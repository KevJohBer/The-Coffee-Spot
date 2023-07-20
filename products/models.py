from django.db import models

# Create your models here.


class Product(models.Model):
    """ A model to describe a product """
    name = models.CharField(max_length=100, default='Product')
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')
    category = models.CharField(max_length=30, null=True, blank=True)
    category_id = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    size = models.IntegerField(default=2, blank=True, null=True)
    ingredients = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str_(self):
        return self.name


class Additions(models.Model):
    """ A model to describe an addition to a product """
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')
