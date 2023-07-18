from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDefaultInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    default_address = models.CharField(max_length=40, null=True, blank=True)
    default_postal_code = models.IntegerField(range(10000, 99999), null=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="static/images")

    def has_active_orders(self):
        return self.user.orders.filter(active=True)
