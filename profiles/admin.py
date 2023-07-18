from django.contrib import admin
from .models import Profile, UserDefaultInfo

# Register your models here.


class DefaultInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_address', 'default_postal_code', 'default_city')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'avatar')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserDefaultInfo, DefaultInfoAdmin)
