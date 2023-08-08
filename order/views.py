from django.shortcuts import render, get_object_or_404, redirect
from datetime import timedelta
from django.views import generic, View
from .models import Order, OrderLineItem
from products.models import Product
from .forms import orderForm, SearchForm
from products.forms import productForm
from .utils import prep_time
from profiles.models import Profile
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from .contexts import cart_contents
from products.contexts import additions_contents
from django.db.models import Q
import stripe

# Create your views here.


# Creating orders
class order(LoginRequiredMixin, View):

    """ A view for ordering coffee """
    def get(self, request):
        product_list = Product.objects.all()
        search_form = SearchForm()
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        client_secret = 0
        search_result = []
        query = None
        errormsg = None

        if 'query' in request.GET:
            query = request.GET['query']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            search_result = product_list.filter(queries)

        if request.user.profile.first_name:
            initial_data = {
                'name': request.user.profile.first_name
            }
            order_form = orderForm(data=initial_data)
        else:
            order_form = orderForm()

        if current_cart:
            total = current_cart['total']
            if total > 0:
                stripe_total = round(total * 100)
                stripe.api_key = stripe_secret_key
                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
                client_secret = intent.client_secret

        context = {
            'product_list': product_list,
            'current_cart': current_cart,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': client_secret,
            'search_form': search_form,
            'search_result': search_result,
            'query': query,
            'errormsg': errormsg,
        }

        return render(request, 'order/order.html', context)


@user_passes_test(lambda u: u.is_authenticated)
def add_to_cart(request, item_id, *args, **kwargs):
    """ allows user to add a selected item to cart """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=item_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        cart_keys = list(cart.keys())
        size = request.POST['size']
        milk_type = request.POST['milk_type']
        if 'addition_dict' in request.session:
            additions = request.session.get('addition_dict')
        else:
            additions = None

        contents = {
            'name': product.name,
            'item_id': product.id,
            'size': size,
            'milk': milk_type,
            'additions': additions,
            'quantity': quantity,
        }

        for key in range(1, 50):
            if str(key) not in cart_keys:
                index = key

        comparator = []
        for item in list(cart.values()):
            comparator.append(list(item.values())[:5])

        if list(contents.values())[:5] not in comparator:
            cart[index] = contents
        else:
            for key in cart_keys:
                if list(cart[key].values())[:5] == list(contents.values())[:5]:
                    cart[key]['quantity'] += 1

        if 'addition_dict' in request.session:
            del request.session['addition_dict']
        request.session['cart'] = cart
        return redirect('order')


@user_passes_test(lambda u: u.is_authenticated)
def adjust_cart_items(request):
    """ allows user to increase or decrease amount of selected product """
    index = request.POST.get('index')
    cart = request.session.get('cart', {})
    item = cart[index]
    quantity = item['quantity']

    if request.method == 'POST':
        if request.POST.get('increment'):
            item['quantity'] = quantity + 1
            if item['additions'] != None:
                for addition in item['additions']:
                    item['additions'][addition] += 1

        elif request.POST.get('decrement'):
            if quantity == 1:
                cart.pop(index)
            else:
                item['quantity'] = quantity - 1

    request.session['cart'] = cart
    return redirect('order')


@user_passes_test(lambda u: u.is_authenticated)
def remove_from_cart(request):
    """ removes selected item from cart """
    cart = request.session.get('cart', {})
    index = request.POST['index']
    cart.pop(index)
    request.session['cart'] = cart
    return redirect('order')


@user_passes_test(lambda u: u.is_authenticated)
def order_confirmation(request, *args, **kwargs):
    """ confirms stripe payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if 'cart' in request.session:
        cart = request.session.get('cart', {})
    else:
        return redirect('order')

    if request.method == 'POST':

        form_data = {
            'customer': request.user,
            'name': request.POST['name'],
            'address': request.POST['address'],
            'total_cost': request.POST['total_cost'],
            'to_go': request.POST['to_go']
        }

        form = orderForm(form_data)
        if form.is_valid():
            order = form.save()
            for item in cart.values():
                product = Product.objects.get(id=item['item_id'])
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    size=item['size'],
                    milk_type=item['milk']
                )
                order_line_item.save()
            order.save()
            prep_time(order.id)

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
            }

    return render(request, 'order/order_confirmation.html', context)
