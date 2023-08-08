"""
Subscription App - URLS

urls for subscription app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<subscription_id>', views.subscription_detail, name='subscription'),
    path('confirm/', views.confirm_subscription, name='confirm_subscription')
]
