from django.test import TestCase
from apps.tracker_data.models import NutrientTracker

# Create your tests here.

class NutrientTrackerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.nutrient_tracker = NutrientTracker.objects.create(
            nutrient="potassium",
            amount=100,
        )
    
    def test_model_content(self):
        self.assertEqual(self.nutrient_tracker.nutrient, "potassium")
        self.assertEqual(self.nutrient_tracker.amount, 100)