from django.shortcuts import render, get_object_or_404, redirect, reverse
from datetime import timedelta
from django.views import generic, View
from .models import Product, Order
from .forms import orderForm, productForm
from profiles.models import Profile
from django.http import HttpResponseRedirect
from django.conf import settings
import stripe

# Create your views here.


class order(View):
    """ A view for ordering coffee """
    def get(self, request):

        product_list = Product.objects.all()
        cart_items = []
        total = 0
        product_count = 0
        cart = request.session.get('cart', {})
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        client_secret = 0

        if not stripe_public_key:
            messages.warning(request, 'No public key bud')

        for item_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'total': total,
            })

        order_form = orderForm()

        if cart_items:
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
        }

        return render(request, 'order/order.html', context)


def add_to_cart(request, item_id):
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
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart
    return redirect('order')


def order_confirmation(request, *args, **kwargs):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        total = float(request.POST.get('total'))

        form_data = {
            'customer': request.user,
            'name': request.POST['name'],
            'country': request.POST['country'],
            'city': request.POST['city'],
            'address': request.POST['address'],
            'total_cost': total,
        }

        order_form = orderForm(form_data)
        order = order_form.save()
        for key, value in cart.items():
            item = Product.objects.get(id=key)
            item.quantity = int(value)
            order.product.add(item)

        order.save()

        new_time = order.date + timedelta(minutes=15)

        context = {
            'order': order,
            'new_time': new_time,
            }

    return render(request, 'order/order_confirmation.html', context)


def create_product(request):
    """ A view for admin to create products """

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        form = productForm(data=request.POST)
        if category_id == 1:
            form.category = 'Regular'
        elif category_id == 2:
            form.category = 'Special'
        elif category_id == 3:
            form.category = 'Premium'

        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            context = {}
            form = productForm
            errormsg = 'data did not validate'
            context['form'] = form
            context['errormsg'] = errormsg
            return render(request, 'product/create_product.html', context)

    else:
        form = productForm()

        context = {
            'form': form
            }

        return render(request, 'product/create_product.html', context)
