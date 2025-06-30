from django.test import TestCase
from apps.nutrient_data.models import Nutrient
from apps.nutrient_data.serializers import NutrientSerializer


# Create your tests here.
class NutrientSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testNutrient = Nutrient.objects.create(
            name="potassium",
            meassure_unit="mg",
        )
        cls.serializer = NutrientSerializer(instance=cls.testNutrient)

    def test_serializer_content(self):
        self.assertEqual(self.serializer.data["name"], "potassium")
        self.assertEqual(self.serializer.data["meassure_unit"], "mg")
        self.assertEqual(self.serializer.data["id"], 1)