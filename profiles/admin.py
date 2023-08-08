"""
Profiles App - admin

admin configuration for profiles app
"""

from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    """ profile admin configuration """
    list_display = ('user', 'first_name', 'last_name', 'avatar')


admin.site.register(Profile, ProfileAdmin)
