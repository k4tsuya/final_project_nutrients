from django.test import TestCase
from apps.food_data.models import Ingredient
from apps.nutrient_data.models import Nutrient


# Create your tests here.
class IngredientTestCase(TestCase):
    def setUp(self):
        self.testNutrient = Nutrient.objects.create(
            name="potassium",
            meassure_unit="mg",
        )

        self.testIngredient = Ingredient.objects.create(
            name="raw potatoes",
            nutrition_value=[{"name": "potassium", "value": 100, "unit": "mg"}],
        )

        self.testIngredient.nutrients.add(self.testNutrient)

    def test_ingredient_access(self):
        """check if ingredients can be created and maybe contain some values"""
        test_potato = Ingredient.objects.get(name="raw potatoes")
        self.assertEqual(test_potato.name, "raw potatoes")
        print("checking name went well")
        self.assertEqual(self.testIngredient.nutrients.count(), 1)
        print("checking nutrient count went well")
        self.assertEqual(self.testIngredient.nutrients.first(), self.testNutrient)
        print("checking nutrient went well")
        print("clarification: ", test_potato.nutrients.first(), self.testNutrient)
        self.assertEqual(
            test_potato.nutrition_value,
            [{"name": "potassium", "value": 100, "unit": "mg"}],
        )
        print("checking nutrient value went well")
