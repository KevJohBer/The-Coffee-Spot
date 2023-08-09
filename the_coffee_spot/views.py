"""
The Coffee Spot App - views

views for the coffee spot app
"""

from django.shortcuts import render


def handler404(request, *args, **kwargs):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403(request, *args, **kwargs):
    """ Error Handler 403 - page Not Found """
    return render(request, "errors/403.html", status=403)


def handler500(request, *args, **kwargs):
    """ Error Handler 500 - page Not Found """
    return render(request, "errors/500.html", status=500)
