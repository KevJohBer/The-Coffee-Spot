from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('delete/<item_id>', views.delete_product, name='delete_product'),
    path('edit/<item_id>', views.edit_product, name='edit_product'),
]
