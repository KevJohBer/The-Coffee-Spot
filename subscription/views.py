"""
Subscription App - Views

views for subscription app
"""

from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from order.models import Product
from .models import Subscription
from .forms import SubscriptionForm


# Create your views here.


def subscription_detail(request, subscription_id):
    """ A view to display subscription details """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    customer_email = request.user.email
    subscription_id = int(subscription_id)
    errormsg = None
    if subscription_id == 1:
        price = 20
        subscription_name = 'Regular'
        stripe_price_id = settings.STRIPE_PLAN_REGULAR
        included_drinks = Product.objects.filter(category_id__lt=2)
        about = "if you just want regular black coffee with or without milk and no other fancy additions then this is the subscription for you"
    elif subscription_id == 2:
        price = 40
        subscription_name = 'Special'
        stripe_price_id = settings.STRIPE_PLAN_SPECIAL
        included_drinks = Product.objects.filter(category_id__lt=3)
        about = "If you want more options to you coffee, this subscriptions offers special warm drinks like caffe latte, cappucino or Americano"
    elif subscription_id == 3:
        price = 70
        subscription_name = 'Premium'
        stripe_price_id = settings.STRIPE_PLAN_PREMIUM
        included_drinks = Product.objects.filter(category_id__lt=4)
        about = "If you don’t like limitations, then premium is the subscription for you. Enjoy any drink warm or cold from our menu"

    form = SubscriptionForm()

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=price * 100,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
        setup_future_usage='off_session',
    )
    client_secret = intent.client_secret

    if 'errormsg' in request.session:
        errormsg = request.session['errormsg']

    context = {
        'price': price,
        'about': about,
        'form': form,
        'subscription_id': subscription_id,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
        'stripe_price_id': stripe_price_id,
        'included_drinks': included_drinks,
        'customer_email': customer_email,
        'intent_id': intent.id,
        'subscription_name': subscription_name,
        'errormsg': errormsg,
        }

    return render(request, 'subscription/subscription_detail.html', context)


def confirm_subscription(request):
    """ Handles subscription creation """

    if request.method == 'POST':
        stripe_price_id = request.POST.get('stripe_price_id')
        token = request.POST.get('token')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_method_id = request.POST.get('payment_method_id')
        intent_id = request.POST['intent_id']

        stripe.PaymentIntent.modify(
            intent_id,
            payment_method=payment_method_id
        )
        stripe.PaymentIntent.confirm(
            intent_id
        )
        customer = stripe.Customer.create(
            email=request.user.email,
            source=token,
        )
        stripe_subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'price': stripe_price_id}],
        )
        subscription_id = int(request.POST.get('subscription_id'))
        price = float(request.POST.get('price'))

        form_data = {
            'stripe_subscription_id': stripe_subscription.id,
            'subscription_name': request.POST['subscription_name'],
            'subscription_id': subscription_id,
            'subscriber': request.user,
            'price': price,
            'address': request.POST['address'],
            'city': request.POST['city'],
            'postal_code': request.POST['postal_code'],
        }

        form = SubscriptionForm(form_data, request.POST)

        if form.is_valid():
            if request.user.subscriptions.exists():
                subscription_object = Subscription.objects.filter(subscriber=request.user)[0]
                old_subscription = stripe.Subscription.retrieve(subscription_object.stripe_subscription_id)
                subscription_object.delete()
                old_subscription.cancel()
            subscription = form.save()
            subscription.save()
        else:
            errormsg = 'Whoa! Something went wrong, data did not validate, check your information and try again'
            request.session['errormsg'] = errormsg

    return redirect('subscription', subscription_id=subscription_id)
