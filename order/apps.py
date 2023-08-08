"""
Order App - Apps

App configuration for order app
"""

from django.apps import AppConfig


class OrderConfig(AppConfig):
    """ App configuration for order app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'
