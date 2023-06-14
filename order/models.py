from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from django.contrib.auth.models import User
import uuid

from profiles.models import Profile

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default='Product')
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')
    category = models.CharField(max_length=30, null=True, blank=True)
    category_id = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str_(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    name = models.CharField(max_length=35, null=True, blank=True)
    order_number = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE,)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
