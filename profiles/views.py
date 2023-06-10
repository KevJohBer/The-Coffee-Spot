from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order
from subscription.models import Subscription
from datetime import timedelta
from django.conf import settings
from .forms import profileForm
import stripe

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


def cancel_subscription(request, item_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe.Subscription.retrieve(item_id)
    subscription_object = get_object_or_404(Subscription, stripe_subscription_id=item_id)
    subscription_object.delete()
    subscription.cancel()
    return redirect('view_subscriptions')


def edit_profile(request):
    form = profileForm()

    if request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('uh oh something happened')

    return render(request, 'profiles/edit_profile.html', {'form': form})
