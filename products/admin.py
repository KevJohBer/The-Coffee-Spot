"""
Product App - Admin

Admin configurations for Product App
"""

from django.contrib import admin
from .models import Product, Additions, Rating

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ Admin configuration for Products """
    list_dispay = (
        'name', 'price', 'category', 'category_id', 'rating',
        'ingredients', 'description', 'has_milk'
        )


class AdditionAdmin(admin.ModelAdmin):
    """ Admin configuration for Additions """
    list_display = ('name', 'price')


class RatingAdmin(admin.ModelAdmin):
    """ Admin configuration for Ratings """
    list_display = ('user', 'product', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Additions, AdditionAdmin)
admin.site.register(Rating, RatingAdmin)
