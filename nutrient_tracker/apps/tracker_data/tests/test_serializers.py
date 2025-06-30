from django.test import TestCase
from apps.tracker_data.models import NutrientTracker
from apps.tracker_data.serializers import NutrientTrackerSerializer


# Create your tests here.
class NutrientTrackerSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.nutrient_tracker = NutrientTracker.objects.create(
            nutrient="potassium",
            amount=100,
        )

    def test_nutrient_tracker_serializer(self):
        serializer = NutrientTrackerSerializer(self.nutrient_tracker)
        data = serializer.data
        self.assertEqual(data["nutrient"], "potassium")
        self.assertEqual(data["amount"], 100)