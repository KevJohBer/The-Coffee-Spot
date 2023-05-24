from django.shortcuts import render

# Create your views here.


def profile_page(request):
    """ A view to display user profile """
    return render(request, 'profiles/profile_page.html')
