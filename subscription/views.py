from django.shortcuts import render

# Create your views here.


def subscription_detail(request, subscription_id):
    """ A view to display subscription details """

    if subscription_id == '1':
        about = "if you just want regular black coffee with or without milk and no other fancy additions then this is the subscription for you"
        included_drinks = ['black Coffee', 'Coffee Milk', 'Black Tea']
    elif subscription_id == '2':
        about = "If you want more options to you coffee, this subscriptions offers special warm drinks like caffe latte, cappucino or Americano"
        included_drinks = ['Caffe Latte', 'Cappuccino', 'Flat White', 'Latte Macchiato', 'Cortado', 'Espresso', 'Americano', 'Ice latte', 'Regular coffees']
    elif subscription_id == '3':
        about = "If you don’t like limitations, then premium is the subscription for you. Enjoy any drink warm or cold from our menu"
        included_drinks = ['Hot chocolate', 'Triple Caffe Latte', 'Iced latte Salted Caramel', 'Iced Latte Caramel', 'Iced Latte Mocha', 'Iced Latte Vanilla', 'Iced Chai', 'Cold brew', 'all items from regular and special']

    context = {
        'about': about,
        'included_drinks': included_drinks,
        }

    return render(request, 'subscription/subscription_detail.html', context)
