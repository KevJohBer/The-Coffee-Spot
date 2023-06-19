from .models import Profile
from django.forms import ModelForm, TextInput, ImageField
from django import forms


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['default_address', 'default_postal_code', 'default_city']
        widgets = {
            'default_address': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'placeholder': 'Address',
            }),
            'default_postal_code': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'placeholder': 'Postal Code',
            }),
            'default_city': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #1E0E00',
                'placeholder': 'City',
            }),
        }
