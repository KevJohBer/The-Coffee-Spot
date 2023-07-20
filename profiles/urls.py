from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # main profile page
    path('', views.profile_page, name='profile_page'),
    path('edit/', views.edit_profile, name='edit_profile'),
    # orders
    path('history/', views.order_history, name='order_history'),
    path('cancel/<item_id>', views.cancel_order, name='cancel_order'),
    # subscriptions
    path('subscriptions/', views.view_subscriptions, name='view_subscriptions'),
    path('cancel_subscription/<item_id>', views.cancel_subscription, name='cancel_subscription'),
    # settings
    path('settings/', views.user_settings, name='user_settings')
    # 
]
