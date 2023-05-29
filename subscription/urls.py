from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<subscription_id>', views.subscription_detail, name='subscription')
]
