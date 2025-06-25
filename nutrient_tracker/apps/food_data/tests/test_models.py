from django.test import TestCase
from apps.food_data.models import Ingredient


# Create your tests here.
class IngredientTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Creates a setup for the tests that is faster than using setUp"""
        cls.testIngredient = Ingredient.objects.create(
            name="raw potatoes",
            nutrition_value=[{"name": "potassium", "value": 100, "unit": "mg"}],
        )

    def test_model_content(self):
        self.assertEqual(self.testIngredient.name, "raw potatoes")
        self.assertEqual(
            self.testIngredient.nutrition_value,
            [{"name": "potassium", "value": 100, "unit": "mg"}],
        )
