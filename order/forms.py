from .models import Order, Product
from django.forms import ModelForm, TextInput, ImageField, ChoiceField
from django import forms


class orderForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Drottninggatan 19'),
        ('1', 'Hamngatan 14'),
        ('1', 'Klarabergsgatan 50'),
    )
    address = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #703600',
        })
    )

    class Meta:
        model = Order
        fields = ["customer", "name", "address", "total_cost",]
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


class productForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Regular'),
        ('2', 'Special'),
        ('3', 'Premium'),
    )
    category_id = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #703600',
        })
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'category', 'category_id']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'Name',
            }),
            'price': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'Price',
            }),
            'category_id': forms.Select(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color:  #703600',
                'placeholder': 'Category',
            }),
            'category': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color:  #703600',
                'placeholder': 'Category',
            }),
            'image': forms.FileInput(attrs={
                'class': 'text-right btn btn-outline-light rounded-0 py-3'
            }),
        }
