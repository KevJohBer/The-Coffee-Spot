from .models import Subscription
from django import forms


class subscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'subscriber', 'price', 'billing_address']
