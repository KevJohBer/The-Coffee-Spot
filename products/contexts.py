from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Product, Additions


def additions_contents(request):
    addition_dict = request.session.get('addition_dict', {})
    additions = []
    total = 0
    count = 0
    context = {}

    for item_id, quantity in addition_dict.items():
        addition = get_object_or_404(Additions, id=item_id)
        addition_id = addition.id
        addition_name = addition.name
        quantity = quantity
        total += quantity * addition.price

        additions.append({
            'addition_name': addition_name,
            'addition_id': addition_id,
            'quantity': quantity,
            'total': total,
        })

    context = {
        'additions': additions,
        'total': total
    }
    return context
