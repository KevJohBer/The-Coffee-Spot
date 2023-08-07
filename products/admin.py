from django.contrib import admin
from .models import Product, Additions, Rating

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_dispay = ('name', 'price', 'category', 'category_id', 'rating', 'ingredients', 'description', 'has_milk')


class AdditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Additions, AdditionAdmin)
admin.site.register(Rating, RatingAdmin)
