from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    default_address = models.CharField(max_length=40, null=True, blank=True)
    default_postal_code = models.IntegerField(range(10000, 99999), null=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    avatar = models.ImageField(upload_to=None, default='no image found')

    def __str__(self):
        return self.user.username

    def has_active_orders(self):
        return self.user.orders.filter(active=True)