from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
