"""
Home app - Views

Home app views
"""


from django.shortcuts import render

from order.models import Product

# Create your views here.


def home_page(request):
    """ Displays the home page """

    menu = Product.objects.all()

    return render(request, 'home/index.html', {'menu': menu})
