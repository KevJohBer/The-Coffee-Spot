from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default='Product')
    price = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')
    category = models.CharField(max_length=30, null=True, blank=True)
    category_id = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str_(self):
        return self.name
