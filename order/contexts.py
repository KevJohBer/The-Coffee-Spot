"""
Order App - Contexts

Contexts for order app
"""


from django.shortcuts import get_object_or_404
from products.models import Product, Additions


def cart_contents(request):
    """ returns context for order page """
    cart_items = []
    total = 0
    cart = request.session.get('cart', {})
    context = {}

    for key in list(cart.keys()):
        additions = cart[key]['additions']
        index = key
        adds = {}
        product = get_object_or_404(Product, id=cart[key]['item_id'])
        if request.user.subscriptions.exists():
            subscription = request.user.subscriptions.all()[0].subscription_id
            if product.category_id <= subscription:
                product.price = 0
        total += cart[key]['quantity'] * product.price

        if additions is not None:
            for addition_id, addition_quantity in additions.items():
                addition = get_object_or_404(Additions, id=addition_id)
                total += addition_quantity * addition.price
                adds[addition.name] = addition_quantity

        cart_items.append({
            'item_id': cart[key]['item_id'],
            'quantity': cart[key]['quantity'],
            'product': product,
            'total': total,
            'size': cart[key]['size'],
            'milk_type': cart[key]['milk'],
            'index': index,
            'adds': adds,
        })
        context['cart_items'] = cart_items
        context['total'] = total
    return context
