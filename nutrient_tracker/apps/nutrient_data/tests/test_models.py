from django.test import TestCase
from apps.nutrient_data.models import Nutrient


# Create your tests here.
class NutrientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testNutrient = Nutrient.objects.create(
            name="potassium",
            meassure_unit="mg",
        )
    
    def test_model_content(self):
        self.assertEqual(self.testNutrient.name, "potassium")
        self.assertEqual(self.testNutrient.meassure_unit, "mg")