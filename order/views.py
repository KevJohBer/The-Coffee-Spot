from django.shortcuts import render

# Create your views here.


def order(request):
    """ A view for ordering coffee """
    return render(request, 'order/order.html')
