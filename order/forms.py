from .models import Order, Product
from django import forms


class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "country", "city", "address", "total_cost"]
