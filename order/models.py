"""
Order App - models

models for order app
"""

import uuid

from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.


class Order(models.Model):
    """ A model for orders """
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='orders')
    name = models.CharField(max_length=35)
    order_number = models.UUIDField(
        default=uuid.uuid4, unique=True,
        db_index=True, editable=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(
        max_digits=5, decimal_places=2, null=False)
    active = models.BooleanField(default=True)
    to_go = models.BooleanField(default=True)


class OrderLineItem(models.Model):
    """ A model for order line items """
    order = models.ForeignKey(
        Order, null=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE,)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    size = models.CharField(
        max_length=10, default='Standard', blank=True, null=True)
    milk_type = models.CharField(
        max_length=30, null=True, blank=True, default='Milk')

    def save(self, *args, **kwargs):
        """ saves the total cost of each line item """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
