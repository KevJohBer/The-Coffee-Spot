from django.db import models
from django_countries.fields import CountryField
import uuid

from profiles.models import Profile

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default='Product')
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str_(self):
        return self.name

    def serialize(self):
        return self.__dict__


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    name = models.CharField(max_length=35, null=True, blank=True)
    order_number = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)

    def __str_(self):
        return self.order_number
