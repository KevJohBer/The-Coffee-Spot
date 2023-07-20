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
import stripe

# Create your views here.


# Creating orders
class order(LoginRequiredMixin, View):

    """ A view for ordering coffee """
    def get(self, request):
        product_list = Product.objects.all()
        search_form = SearchForm()
        cart_items = []
        total = 0
        product_count = 0
        cart = request.session.get('cart', {})
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        client_secret = 0
        search_result = []
        query = None
        errormsg = None

        if 'query' in request.GET:
            query = request.GET['query']
            count = Product.objects.all().count()
            for product in product_list:
                if query.lower() == product.name.lower():
                    search_result.append(product)
                else:
                    count -= 1
                    if count == 0:
                        errormsg = f'sorry, we could not find a result for "{query}"'

        for item_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            if request.user.subscriptions.exists():
                subscription = request.user.subscriptions.all()[0].subscription_id
                if product.category_id <= subscription:
                    product.price = 0
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'total': total,
                'product_count': product_count,
            })

        order_form = orderForm()

        if cart_items and total >= 1:
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            client_secret = intent.client_secret

        context = {
            'product_list': product_list,
            'cart_items': cart_items,
            'total': total,
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
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        redirect_url = request.POST.get('redirect_url')

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        return redirect(redirect_url)

def adjust_cart_items(request, item_id):
    """ allows user to increase or decrease amount of selected product """
    cart = request.session.get('cart', {})
    quantity = cart.get(item_id)

    if request.method == 'POST':
        if request.POST.get('increment'):
            cart[item_id] = quantity + 1
        elif request.POST.get('decrement'):
            cart[item_id] = quantity - 1

    request.session['cart'] = cart
    return redirect('order')

def remove_from_cart(request, item_id):
    """ removes selected item from cart """
    cart = request.session.get('cart', {})
    cart.pop(item_id)
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

