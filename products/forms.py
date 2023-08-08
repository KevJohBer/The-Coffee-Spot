"""
Product App - Forms

Forms for product app
"""


from django.forms import ModelForm, TextInput, ImageField, ChoiceField
from django import forms
from .models import Product, Rating


class ProductForm(forms.ModelForm):
    """ A form for creating products """
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
    HAS_MILK = (
        ('True', 'Milk'),
        ('False', 'No Milk')
    )
    has_milk = forms.ChoiceField(choices=HAS_MILK, widget=forms.Select(attrs={
        'class': "form-control rounded-0 border-light text-white",
        'style': 'background-color:  #703600',
    }))

    class Meta:
        """ Meta for ProductForm """
        model = Product
        fields = [
            'name', 'price', 'image', 'category',
            'category_id', 'has_milk', 'ingredients',
            'description'
            ]
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
            'image': forms.FileInput(attrs={
                'class': 'text-right btn btn-outline-light rounded-0 py-3'
            }),
            'has_milk': forms.Select(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color:  #703600',
                'placeholder': 'Has Milk',
            }),
            'ingredients': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'ingredients',
            }),
            'description': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'placeholder': 'description',
            }),
        }


class RatingForm(forms.ModelForm):
    """ A form for rating products """
    class Meta:
        """ Meta for RatingForm"""
        model = Rating
        fields = ['rating']
