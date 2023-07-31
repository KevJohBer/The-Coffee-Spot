from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('delete/<item_id>', views.delete_product, name='delete_product'),
    path('edit/<item_id>', views.edit_product, name='edit_product'),
    path('product_details/<item_id>', views.product_details, name='product_details'),
    path('customize_product/<item_id>', views.customize_product, name='customize_product'),
    # Additions
    path('addition/<product_id>/<item_id>', views.addition, name='addition'),
    path('delete_addition/<item_id>', views.delete_addition, name='delete_addition'),
    path('adjust_addition/<item_id>', views.adjust_additions, name='adjust_addition'),
]
