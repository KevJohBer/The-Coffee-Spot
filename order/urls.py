from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order.as_view(), name='order'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>', views.adjust_cart_items, name='adjust_cart_items'),
    path('remove/<item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('confirmation/', views.order_confirmation, name='order_confirmation'),
    path('create/', views.create_product, name='create_product'),
    path('delete/<item_id>', views.delete_product, name='delete_product'),
    path('edit/<item_id>', views.edit_product, name='edit_product'),
    path('search/', views.search_products, name='search_products'),
]
