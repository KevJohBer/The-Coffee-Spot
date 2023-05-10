from django.db import models

# Create your models here.


class Product(models.model):
    name = models.CharField(max_length=250, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    address = models.Charfield(max_length=100, null=True, blank=True)
    date = models.DatetimeField(auto_now_add=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
