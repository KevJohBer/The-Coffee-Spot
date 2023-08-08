from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order, OrderLineItem
from subscription.models import Subscription
from datetime import timedelta
from django.conf import settings
from .forms import profileForm, InfoForm
from django.contrib.auth.decorators import user_passes_test
import stripe

# Profile page


@user_passes_test(lambda u: u.is_authenticated)
def profile_page(request):
    """ A view to display user profile """
    return render(request, 'profiles/profile_page.html')


@user_passes_test(lambda u: u.is_authenticated)
def edit_profile(request):
    """ Allows user to edit their profile """
    form = profileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
        else:
            form = profileForm()
            errormsg = 'Whoa! Something went wrong, data did not validate, check your information and try again'
            return render(request, 'profiles/edit_profile.html', {'form': form, 'errormsg': errormsg})
    return render(request, 'profiles/edit_profile.html', {'form': form})


# Orders

@user_passes_test(lambda u: u.is_authenticated)
def order_history(request):
    """ Shows users order history """
    orders = Order.objects.filter(customer=request.user)
    orders = orders.order_by('-date')
    context = {}
    if orders:
        context['orders'] = orders

    return render(request, 'profiles/profile_page.html', context)


@user_passes_test(lambda u: u.is_authenticated)
def cancel_order(request, item_id):
    """ Gives user the option to cancel an order """
    order = get_object_or_404(Order, pk=item_id)
    order.delete()
    return redirect('order_history')

# subscriptions


@user_passes_test(lambda u: u.is_authenticated)
def view_subscriptions(request):
    """ shows users their subscription """
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    context = {'subscriptions': subscriptions, 'request': request}
    return render(request, 'profiles/profile_page.html', context,)


@user_passes_test(lambda u: u.is_authenticated)
def cancel_subscription(request, item_id):
    """ Gives user the option to cancel their subscription """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe.Subscription.retrieve(item_id)
    subscription_object = get_object_or_404(Subscription, stripe_subscription_id=item_id)
    subscription_object.delete()
    subscription.cancel()
    return redirect('view_subscriptions')


@user_passes_test(lambda u: u.is_authenticated)
def user_settings(request):
    """ A view to let users change settings on their experience """
    form = InfoForm(instance=request.user.profile)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_settings')
        else:
            form = InfoForm()
            errormsg = 'Whoa! Something went wrong, data did not validate, check your information and try again'
            return render(request, "profiles/profile_page.html", {'form': form, 'errormsg': errormsg})
    return render(request, "profiles/profile_page.html", {'form': form})
