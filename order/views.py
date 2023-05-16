from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Product, Order
from django.http import HttpResponseRedirect

# Create your views here.


class order(View):
    """ A view for ordering coffee """
    def get(self, request):

        product_list = Product.objects.all()
        cart_items = []
        total = 0
        product_count = 0
        cart = request.session.get('cart', {})

        for item_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

        context = {
            'product_list': product_list,
            'cart_items': cart_items,
            'total': total,
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
