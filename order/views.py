from django.shortcuts import render
from .models import Product, Order

# Create your views here.


def order(request):
    """ A view for ordering coffee """

    product_list = Product.objects.all()

    context = {'product_list': product_list}

    return render(request, 'order/order.html', context)
