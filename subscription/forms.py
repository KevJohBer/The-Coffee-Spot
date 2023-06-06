from .models import Subscription
from django import forms


class subscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscription_id', 'subscription_name', 'subscriber', 'price', 'billing_address']
        widgets = {
            'billing_address': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'Billing Address',
            })
        }
