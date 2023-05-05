from django.shortcuts import render

# Create your views here.


def home_page(request):
    """ Displays the home page """
    return render(request, 'home/index.html')
