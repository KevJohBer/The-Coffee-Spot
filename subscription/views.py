from django.shortcuts import render

# Create your views here.


def subscription_detail(request):
    """ A view to display subscription details """
    return render(request, 'subscription/subscription_detail.html')
