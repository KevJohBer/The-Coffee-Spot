from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Product, Additions


def additions_contents(request):
    addition_dict = request.session.get('addition_dict', {})
    additions = []
    total = 0
    count = 0
    context = {}

    for item in addition_dict.values():
        addition_id = item['addition_id']
        addition_name = item['addition_name']
        quantity = int(item['quantity'])
        addition = get_object_or_404(Additions, id=addition_id)
        total += quantity * addition.price
        count += quantity

        additions.append({
            'addition_id': addition_id,
            'addition_name': addition_name,
            'quantity': quantity,
            'addition': addition,
            'total': total,
            'count': count
        })

    context = {
        'additions': additions,
        'total': total
    }
    return context
