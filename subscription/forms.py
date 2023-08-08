"""
Subscription App - forms

forms for subscription app
"""

from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    """ form for creating subscription """
    class Meta:
        """ SubscriptionForm meta """
        model = Subscription
        fields = [
            'subscription_id', 'stripe_subscription_id',
            'subscription_name', 'subscriber', 'price',
            'address', 'city', 'postal_code'
            ]
        widgets = {
            'address': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'Address',
            }),
            'city': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'City',
            }),
            'postal_code': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'Postal Code xxxxx',
            }),
        }
