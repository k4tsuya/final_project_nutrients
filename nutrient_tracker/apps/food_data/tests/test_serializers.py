from django.test import TestCase
from apps.food_data.models import Ingredient
from apps.food_data.serializers import IngredientDataSerializer


# Create your tests here.
class IngredientDataSerializerTests(TestCase):
    def setUp(self):
        self.testIngredient = Ingredient.objects.create(
            name="raw potatoes",
            nutrition_value=[{"name": "potassium", "value": 100, "unit": "mg"}],
        )
        self.serializer = IngredientDataSerializer(instance=self.testIngredient)

    def test_serializer_content(self):
        self.assertEqual(self.serializer.data["name"], "raw potatoes")
        self.assertEqual(
            self.serializer.data["nutrition_value"],
            [{"name": "potassium", "value": 100, "unit": "mg"}],
        )
        self.assertEqual(self.serializer.data["id"], 1)

        self.assertEqual(
            self.serializer.data["nutrients"],
            [{"name": "potassium", "value": 100, "unit": "mg"}],
        )
