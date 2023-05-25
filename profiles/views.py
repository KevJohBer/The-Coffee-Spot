from django.shortcuts import render
from order.models import Order

# Create your views here.


def profile_page(request):
    """ A view to display user profile """
    user = request.user.profile
    orders = Order.objects.filter(customer=user)

    context = {'orders': orders}
    return render(request, 'profiles/profile_page.html', context)
