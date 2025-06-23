from django.test import TestCase
from django.db import connection
from apps.user_info.models import User, Profile, Favorite, History, TrackedNutrients


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creates a setup for the tests that is faster than using setUp"""
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.profile = Profile.objects.create(user=cls.user)
        cls.favorites = Favorite.objects.create(user=cls.user)
        cls.history = History.objects.create(user=cls.user)
        cls.tracked_nutrients = TrackedNutrients.objects.create(user=cls.user)

    def test_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.password, "testpassword")
