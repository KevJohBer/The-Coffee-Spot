from django.contrib import admin
from .models import Subscription

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscriber', 'price', 'billing_address')


admin.site.register(Subscription, SubscriptionAdmin)
