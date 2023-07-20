from .models import Order
from django.forms import ModelForm, TextInput, ImageField, ChoiceField
from django import forms


class orderForm(forms.ModelForm):
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
        model = Order
        fields = ["customer", "name", "address", "total_cost"]
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
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #703600; width: 50%;',
        'placeholder': 'Search for drinks',
        })
    )
