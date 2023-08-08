"""
Order App - Forms

Forms for Order App
-orderForm
-searchForm
-customLineItemForm
"""

from django.forms import ModelForm, TextInput, ImageField, ChoiceField
from django import forms
from .models import Order, OrderLineItem



class OrderForm(forms.ModelForm):
    """ A form to let users make an order """
    CHOICES = (
        ('Drottninggatan 19', 'Drottninggatan 19'),
        ('Hamngatan 14', 'Hamngatan 14'),
        ('Klarabergsgatan 50', 'Klarabergsgatan 50'),
    )
    address = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #1E0E00',
        })
    )

    class Meta:
        """ OrderForm Meta """
        model = Order
        fields = ["customer", "name", "address", "total_cost", "to_go"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'placeholder': 'Name',
            }),
            'address': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'placeholder': 'Address',
            }),
            'to_go': forms.CheckboxInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'label': 'To-go',
            })
        }


class SearchForm(forms.Form):
    """ A form to let users search for products """
    query = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #703600; width: 50%;',
        'placeholder': 'Search for drinks',
        })
    )


class CustomLineItemForm(forms.ModelForm):
    """ A form to let users customize order line items """
    OPTIONS1 = (
        ('Standard', 'Standard'),
        ('Small', 'Small'),
    )
    size = forms.ChoiceField(choices=OPTIONS1, widget=forms.RadioSelect())

    OPTIONS2 = (
        ('Milk', 'Milk'),
        ('Non Lactose Milk', 'Non Lactose Milk'),
        ('Oat Milk', 'Oat Milk'),
        ('Soy Milk', 'Soy Milk'),
        ('Coconut Milk', 'Coconut Milk'),
    )
    milk_type = forms.ChoiceField(choices=OPTIONS2, widget=forms.RadioSelect(attrs={
        'style': 'background-color:  #703600; width: 50%;',
    }))

    class Meta:
        """  CustomLineItemForm Meta """
        model = OrderLineItem
        fields = ['size', 'milk_type']
