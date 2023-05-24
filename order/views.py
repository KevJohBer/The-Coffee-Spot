from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Product, Order
from .forms import orderForm
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

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'product_list': product_list,
            'cart_items': cart_items,
            'total': total,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
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
        current_cart = request.POST.get('cart_items')
        total = float(request.POST.get('total'))

        form_data = {
            'name': request.POST['name'],
            'country': request.POST['country'],
            'city': request.POST['city'],
            'address': request.POST['address'],
            'total_cost': total,
        }

        order_form = orderForm(form_data)
        order_form.save()

    return render(request, 'order/order_confirmation.html')
