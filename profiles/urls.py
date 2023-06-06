from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('history/', views.order_history, name='order_history'),
    path('subscriptions', views.view_subscriptions, name='view_subscriptions'),
]
