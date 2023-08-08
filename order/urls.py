"""
Order App - URLS

urls for order app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderView.as_view(), name='order'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('adjust/', views.adjust_cart_items, name='adjust_cart_items'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('confirmation/', views.order_confirmation, name='order_confirmation'),
]
