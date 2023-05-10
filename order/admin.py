from django.contrib import admin
from .models import Product, Order

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_dispay = ('name', 'price')


admin.site.register(Product, ProductAdmin)
