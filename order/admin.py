from django.contrib import admin
from .models import Product, Order

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_dispay = ('name', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'order_number', 'address', 'date', 'total_cost',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
