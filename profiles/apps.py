"""
Profiles App - Apps

app configuration for profiles app
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ configures profile app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        """ imports profile signals """
        import profiles.signals
