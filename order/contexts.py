from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Additions


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    context = {}

    for key in list(cart.keys()):
        item_id = cart[key]['item_id']
        quantity = cart[key]['quantity']
        size = cart[key]['size']
        milk_type = cart[key]['milk']
        additions = cart[key]['additions']
        index = key
        adds = {}
        product = get_object_or_404(Product, id=item_id)
        if request.user.subscriptions.exists():
            subscription = request.user.subscriptions.all()[0].subscription_id
            if product.category_id <= subscription:
                product.price = 0
        total += quantity * product.price

        if additions != None:
            for addition_id, addition_quantity in additions.items():
                addition = get_object_or_404(Additions, id=addition_id)
                total += addition_quantity * addition.price
                adds[addition.name] = addition_quantity

        product_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'total': total,
            'product_count': product_count,
            'size': size,
            'milk_type': milk_type,
            'index': index,
            'adds': adds,
        })
        context['cart_items'] = cart_items
        context['total'] = total
    return context
