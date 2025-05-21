from django.test import TestCase
from apps.user_info.models import User, Favorite, History
from apps.nutrient_data.models import Nutrient
from apps.tracker_data.models import NutrientTracker

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            role="user",
            email="mB2Rw@example.com",
            password="testpassword",
            gender="male",
        )

        self.nutrient = Nutrient.objects.create(name="testnutrient", meassure_unit="mg")
        self.tracker = NutrientTracker.objects.create(
            user=self.user,
            min=0,
            max=100,
            current_value=50,
            date="2022-01-01",
            nutrient=self.nutrient,
        )
        self.favorite = Favorite.objects.create(user=self.user)
        self.history = History.objects.create(user=self.user)

    def tearDown(self):
        self.user.delete()
        self.favorite.delete()
        self.history.delete()

    def test_user_creation_success(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.role, "user")
        self.assertEqual(self.user.email, "mB2Rw@example.com")
        self.assertEqual(self.user.password, "testpassword")
        self.assertEqual(self.user.gender, "male")

        self.assertEqual(self.favorite.user, self.user)
        self.assertEqual(self.history.user, self.user)

    def test_user_creation_fail(self):
        self.assertNotEqual(self.user.username, "testuser2")
        self.assertNotEqual(self.user.role, "admin")
        self.assertNotEqual(self.user.email, "mB2Rw@exomple.com")
        self.assertNotEqual(self.user.password, "testpgssword")
        self.assertNotEqual(self.user.gender, "female")

    def test_history_access_success(self):
        self.assertEqual(self.history.user, self.user)
        self.assertEqual(self.history.nutrient.count(), 0)  # amount of history entries
        self.assertEqual(
            self.history.ingredient.count(), 0
        )  # amount of history entries
        self.assertEqual(self.history.recipe.count(), 0)  # amount of history entries

    def test_history_access_fail(self):
        self.assertEqual(self.history.user, self.user)
        self.assertNotEqual(
            self.history.nutrient.count(), 1
        )  # amount of history entries
        self.assertNotEqual(
            self.history.ingredient.count(), 1
        )  # amount of history entries
        self.assertNotEqual(self.history.recipe.count(), 1)  # amount of history entries

    def test_favorite_access(self):
        self.assertEqual(self.favorite.user, self.user)
        self.assertEqual(self.favorite.nutrient.count(), 0)
        self.assertEqual(self.favorite.ingredient.count(), 0)
        self.assertEqual(self.favorite.recipe.count(), 0)

    def test_favorite_access_fail(self):
        self.assertEqual(self.favorite.user, self.user)
        self.assertNotEqual(self.favorite.nutrient.count(), 1)
        self.assertNotEqual(self.favorite.ingredient.count(), 1)
        self.assertNotEqual(self.favorite.recipe.count(), 1)
