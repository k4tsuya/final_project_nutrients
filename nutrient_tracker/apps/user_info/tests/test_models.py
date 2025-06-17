from django.test import TestCase
from django.db import connection
from apps.user_info.models import User, Profile, Favorite, History, TrackedNutrients


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creates a setup for the tests that is faster than using setUp"""
        model1 = User
        model2 = Profile
        model3 = Favorite
        model4 = History
        model5 = TrackedNutrients
        model = [model1, model2, model3, model4, model5]
        with connection.schema_editor() as editor:
            editor.create_model(model)
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
