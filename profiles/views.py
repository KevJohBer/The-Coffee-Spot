from django.shortcuts import render
from order.models import Order
from subscription.models import Subscription
from datetime import timedelta

# Create your views here.


def profile_page(request):
    """ A view to display user profile """
    return render(request, 'profiles/profile_page.html')


def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    context = {}
    if orders:
        for order in orders:
            new_time = order.date + timedelta(minutes=15)
            context['new_time'] = new_time

    context['orders'] = orders

    return render(request, 'profiles/profile_page.html', context)


def view_subscriptions(request):
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    context = {'subscriptions': subscriptions, 'request': request}
    return render(request, 'profiles/profile_page.html', context,)
