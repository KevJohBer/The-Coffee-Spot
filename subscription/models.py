from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscription(models.Model):
    name = models.IntegerField(default=0)
    subscriber = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_address = models.CharField(max_length=40, null=True, blank=True)
