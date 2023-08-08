"""
Product App - Apps

App configurations for products
"""

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ App configuration for products """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
