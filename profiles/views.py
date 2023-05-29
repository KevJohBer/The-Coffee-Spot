from django.shortcuts import render
from order.models import Order
from datetime import timedelta

# Create your views here.


def profile_page(request):
    """ A view to display user profile """
    orders = Order.objects.filter(customer=request.user)
    for order in orders:
        new_time = order.date + timedelta(minutes=15)

    context = {
        'orders': orders,
        'new_time': new_time,
        }
    return render(request, 'profiles/profile_page.html', context)
