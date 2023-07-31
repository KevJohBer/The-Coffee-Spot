from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Additions


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    context = {}

    for item in cart.values():
        item_id = item['item_id']
        quantity = item['quantity']
        size = item['size']
        milk_type = item['milk_type']
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
            'size': size,
            'milk_type': milk_type,
        })
        context['cart_items'] = cart_items
        context['total'] = total
    return context
