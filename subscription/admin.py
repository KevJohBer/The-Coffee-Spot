"""
Subscription App - Admin

admin configuration for subscription app
"""

from django.contrib import admin
from .models import Subscription

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    """ admin configuration for subscriptions """
    list_display = (
        'subscription_id', 'subscription_name', 'subscriber',
        'price', 'address', 'city', 'postal_code', 'date'
        )


admin.site.register(Subscription, SubscriptionAdmin)
