from django.test import TestCase
from apps.tracker_data.models import NutrientTracker
from apps.nutrient_data.models import Nutrient
from apps.user_info.models import User

# Create your tests here.


class NutrientTrackerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.nutrient = Nutrient.objects.create(
            name="testnutrient", meassure_unit="mg"
        )
        self.tracker = NutrientTracker.objects.create(
            user=self.user,
            min=0,
            max=100,
            current_value=50,
            date="2022-01-01",
            nutrient=self.nutrient,
        )

    def test_nutrient_tracker_access_success(self):
        self.assertEqual(self.tracker.user, self.user)
        self.assertEqual(self.tracker.nutrient, self.nutrient)
        self.assertEqual(self.tracker.min, 0)
        self.assertEqual(self.tracker.max, 100)
        self.assertEqual(self.tracker.current_value, 50)
        self.assertEqual(self.tracker.date, "2022-01-01")

    def test_nutrient_tracker_access_fail(self):
        self.assertNotEqual(self.tracker.user, "guy")
        self.assertNotEqual(self.tracker.nutrient, "validnutrient")
        self.assertNotEqual(self.tracker.min, 3)
        self.assertNotEqual(self.tracker.max, 10)
        self.assertNotEqual(self.tracker.current_value, 5)
        self.assertNotEqual(self.tracker.date, "2025-01-21")
