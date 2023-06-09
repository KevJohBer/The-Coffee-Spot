from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order, OrderLineItem
from subscription.models import Subscription
from datetime import timedelta
from django.conf import settings
from .forms import profileForm
import stripe

# Profile page


def profile_page(request):
    """ A view to display user profile """
    return render(request, 'profiles/profile_page.html')


def edit_profile(request):
    """ Allows user to edit their profile """
    form = profileForm()

    if request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
        else:
            form = profileForm()
            print('uh oh something happened')
            return render(request, 'profiles/edit_profile', {'form': form})
    return render(request, 'profiles/edit_profile.html', {'form': form})


# Orders

def order_history(request):
    """ Shows users order history """
    orders = Order.objects.filter(customer=request.user)
    orders = orders.order_by('-date')
    context = {}
    if orders:
        context['orders'] = orders

    return render(request, 'profiles/profile_page.html', context)


def cancel_order(request, item_id):
    """ Gives user the option to cancel an order """
    order = get_object_or_404(Order, pk=item_id)
    order.delete()
    return redirect('order_history')

# subscriptions


def view_subscriptions(request):
    """ shows users their subscription """
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    context = {'subscriptions': subscriptions, 'request': request}
    return render(request, 'profiles/profile_page.html', context,)


def cancel_subscription(request, item_id):
    """ Gives user the option to cancel their subscription """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe.Subscription.retrieve(item_id)
    subscription_object = get_object_or_404(Subscription, stripe_subscription_id=item_id)
    subscription_object.delete()
    subscription.cancel()
    return redirect('view_subscriptions')
