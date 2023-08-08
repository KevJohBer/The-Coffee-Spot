"""
Subscription App - Apps

app configuration for subscription app
"""

from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    """ app configuration for subscriptions """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'
