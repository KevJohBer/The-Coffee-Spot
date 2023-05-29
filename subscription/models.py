from django.db import models
from django.contrib.auth.models import User
from order.models import Product

# Create your models here.


class Subcription(models.Model):
    name = models.CharField(max_length=100, default='subscription')
    subscriber = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    included_products = models.ManyToManyField(Product)
    description = models.TextField(max_length=1000, default='subscription_info')
