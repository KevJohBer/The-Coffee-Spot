from django.contrib import admin
from .models import Product, Order, OrderLineItem

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_dispay = ('name', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'order_number', 'address', 'date', 'total_cost')


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'size', 'milk_type', 'lineitem_total')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
