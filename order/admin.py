"""
Order App - admin

Admin configuration for order app
"""

from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    """ Admin configuration for orders """
    list_display = (
        'customer', 'name', 'order_number', 'address', 'date', 'total_cost')


class OrderLineItemAdmin(admin.ModelAdmin):
    """ Admin configuration for order line items """
    list_display = (
        'order', 'product', 'quantity', 'size', 'milk_type', 'lineitem_total')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
