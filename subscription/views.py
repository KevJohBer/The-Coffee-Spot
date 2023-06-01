from django.shortcuts import render
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
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sub_id = int(subscription_id)
    if sub_id == 1:
        price = 20
        stripe_plan_id = settings.STRIPE_PLAN_REGULAR
        included_drinks = Product.objects.filter(category_id=sub_id)
        about = "if you just want regular black coffee with or without milk and no other fancy additions then this is the subscription for you"
    elif sub_id == 2:
        price = 40
        stripe_plan_id = settings.STRIPE_PLAN_SPECIAL
        included_drinks = Product.objects.filter(Q(category_id=1) | Q(category_id=2))
        about = "If you want more options to you coffee, this subscriptions offers special warm drinks like caffe latte, cappucino or Americano"
    elif sub_id == 3:
        price = 70
        stripe_plan_id = settings.STRIPE_PLAN_PREMIUM
        included_drinks = Product.objects.all
        about = "If you don’t like limitations, then premium is the subscription for you. Enjoy any drink warm or cold from our menu"

    form = subscriptionForm()

    stripe_total = round(price * 100)

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        payment_method_types=['card'],
    )
    client_secret = intent.client_secret

    context = {
        'price': price,
        'about': about,
        'form': form,
        'sub_id': sub_id,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
        'stripe_plan_id': stripe_plan_id,
        'included_drinks': included_drinks,
        }

    return render(request, 'subscription/subscription_detail.html', context)


def confirm_subscription(request):
    """ Handles subscription creation """

    if request.method == 'POST':
        stripe_plan_id = request.POST.get('stripe_plan_id')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_method_id = request.POST.get('payment_method_id')
        print(f'{payment_method_id} over here!')
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id
        )
        customer.payment_method = request.POST.get('payment_method', 'card')
        stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id,
                }
            ],
        )

        name = int(request.POST.get('sub_id'))
        price = float(request.POST.get('price'))

        form_data = {
            'name': name,
            'subscriber': request.user,
            'price': price,
        }

        form = subscriptionForm(form_data)

        if form.is_valid():
            subscription = form.save()
            subscription.save()
            context = {
                'stripe_subscription': stripe_subscription,
                'product': product,
            }
     
            render(request, 'subscription/subscription_detail.html', context)
        else:
            print(form.errors)

    return render(request, 'subscription/subscription_detail.html')
