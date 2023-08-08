"""
Profiles App - forms

forms for profiles app
"""

from django.forms import ModelForm, TextInput, ImageField
from django import forms
from .models import Profile


class InfoForm(forms.ModelForm):
    """ form for default information """
    class Meta:
        """ InfoForm Meta """
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


class ProfileForm(forms.ModelForm):
    """ Form for editing profiles """
    class Meta:
        """ ProfileForm Meta """
        model = Profile
        fields = ['first_name', 'last_name', 'description', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
                'rows': 3,
            }),
            'avatar': forms.FileInput(attrs={
                'class': "form-control rounded-0 border-light text-white",
                'style': 'background-color: #703600',
            }),
        }
