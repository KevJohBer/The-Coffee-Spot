from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address = models.CharField(max_length=40, null=True, blank=True)
    default_postal_code = models.IntegerField(range(10000, 99999))
    default_city = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username
