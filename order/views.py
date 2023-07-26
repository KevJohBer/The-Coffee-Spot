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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .contexts import cart_contents
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
            if product_list.filter(name=query).exists():
                product = get_object_or_404(Product, name=query)
                search_result.append(product)
            else:
                errormsg = f'sorry, we could not find a result for "{query}"'

        order_form = orderForm()

        if current_cart:
            total = current_cart['total']
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


def add_to_cart(request, item_id):
    """ allows user to add a selected item to cart """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=item_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        size = request.POST['size']
        milk_type = request.POST['milk_type']

        if item_id in list(cart.keys()):
            quantity += quantity

        cart[str(product.name)] = {
            'item_id': item_id,
            'quantity': quantity,
            'size': size,
            'milk_type': milk_type
        }

        request.session['cart'] = cart
        return redirect('order')


def adjust_cart_items(request, item_id):
    """ allows user to increase or decrease amount of selected product """
    product = get_object_or_404(Product, id=item_id)
    cart = request.session.get('cart', {})
    item = cart[str(product.name)]
    quantity = item['quantity']

    if request.method == 'POST':
        if request.POST.get('increment'):
            item['quantity'] = quantity + 1
        elif request.POST.get('decrement'):
            if quantity < 1:
                item['quantity'] = quantity - 1
            else:
                cart.pop(str(product.name))

    request.session['cart'] = cart
    return redirect('order')


def remove_from_cart(request, item_id):
    """ removes selected item from cart """
    product = get_object_or_404(Product, id=item_id)
    cart = request.session.get('cart', {})
    cart.pop(str(product.name))
    request.session['cart'] = cart
    return redirect('order')


def order_confirmation(request, *args, **kwargs):
    """ confirms stripe payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'customer': request.user,
            'name': request.POST['name'],
            'address': request.POST['address'],
            'total_cost': request.POST['total'],
        }

        form = orderForm(form_data)
        if form.is_valid:
            order = form.save()
            for item_id, quantity in cart.items():
                item = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=item,
                    quantity=quantity,
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
