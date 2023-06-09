from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_address', 'default_postal_code', 'default_city')


admin.site.register(Profile, ProfileAdmin)
