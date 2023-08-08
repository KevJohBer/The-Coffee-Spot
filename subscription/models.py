"""
Subscription App - models

models for Subscription App
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscription(models.Model):
    """ A model to define a subscription """
    subscription_id = models.IntegerField(default=0)
    subscription_name = models.CharField(max_length=30, blank=True, null=True)
    stripe_subscription_id = models.CharField(
        max_length=100, blank=True, null=True)
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False, blank=False, related_name='subscriptions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=40, null=True, blank=True)
    postal_code = models.IntegerField(range(10000, 99999))
    city = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
