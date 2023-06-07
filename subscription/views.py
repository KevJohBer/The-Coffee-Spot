from django.shortcuts import render, redirect
from .forms import subscriptionForm
from django.conf import settings
from profiles.models import Profile
from order.models import Product
from django.db.models import Q
import stripe

# Create your views here.


def subscription_detail(request, subscription_id):
    """ A view to display subscription details """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    customer_email = request.user.email
    subscription_id = int(subscription_id)
    if subscription_id == 1:
        price = 20
        subscription_name = 'Regular'
        stripe_price_id = settings.STRIPE_PLAN_REGULAR
        included_drinks = Product.objects.filter(category_id=subscription_id)
        about = "if you just want regular black coffee with or without milk and no other fancy additions then this is the subscription for you"
    elif subscription_id == 2:
        price = 40
        subscription_name = 'Special'
        stripe_price_id = settings.STRIPE_PLAN_SPECIAL
        included_drinks = Product.objects.filter(Q(category_id=1) | Q(category_id=2))
        about = "If you want more options to you coffee, this subscriptions offers special warm drinks like caffe latte, cappucino or Americano"
    elif subscription_id == 3:
        price = 70
        subscription_name = 'Premium'
        stripe_price_id = settings.STRIPE_PLAN_PREMIUM
        included_drinks = Product.objects.all
        about = "If you don’t like limitations, then premium is the subscription for you. Enjoy any drink warm or cold from our menu"

    form = subscriptionForm()

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=price * 100,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
        setup_future_usage='off_session',
    )
    client_secret = intent.client_secret

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
        subscription_name = request.POST.get('subscription_name')
        price = float(request.POST.get('price'))

        form_data = {
            'stripe_subscription_id': stripe_subscription.id,
            'subscription_id': subscription_id,
            'subscription_name': subscription_name,
            'subscriber': request.user,
            'price': price,
        }

        form = subscriptionForm(form_data)

        if form.is_valid():
            subscription = form.save()
            subscription.save()
            return redirect('view_subscriptions')
        else:
            print(form.errors)

    return render(request, 'subscription/subscription_detail.html')