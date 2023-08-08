"""
Profiles App - Test

Automatic tests for profiles app
"""

from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile


class TestProfile(TestCase):
    """ tests for profiles app """
    def setUp(self):
        """ sets up test environment """
        self.user = User.objects.create_user(username='testuser', password='test')

        login = self.client.login(username='testuser', password='test')

    def tearDown(self):
        """ tears down test environment """
        Profile.objects.all().delete()

    def test_profile_creation(self):
        """ tests if a profile is created automatically on user sign up """
        self.assertTrue(Profile.objects.filter(user=self.user).exists())
