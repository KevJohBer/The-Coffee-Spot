from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str_(self):
        return self.name

    def serialize(self):
        return self.__dict__


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)

    def __str_(self):
        return self.order_number
