from django.contrib.auth.models import User
from .models import Profile
from django.test import TestCase
from . import views
from order.models import Order


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test')

        login = self.client.login(username='testuser', password='test')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_profile_creation(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())
