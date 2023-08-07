from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.


class Product(models.Model):
    """ A model to describe a product """
    name = models.CharField(max_length=100, default='Product')
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='static/images', default='static/images/coffee-cup.png')
    category = models.CharField(max_length=30, null=True, blank=True)
    category_id = models.IntegerField(default=0)
    ingredients = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    has_milk = models.BooleanField(default=True)

    def __str_(self):
        return self.name

    def average_rating(self):
        if self.ratings.exists():
            average_rating = self.ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
            return round(average_rating, 1)
        else:
            return None


class Additions(models.Model):
    """ A model to describe an addition to a product """
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')


class Rating(models.Model):
    """ A model to let user rate a product """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)
