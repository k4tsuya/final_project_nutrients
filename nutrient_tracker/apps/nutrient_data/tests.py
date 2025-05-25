from django.test import TestCase
from apps.nutrient_data.models import Nutrient


# Create your tests here.
class NutrientTestCase(TestCase):
    def setUp(self):
        self.testNutrient1 = Nutrient.objects.create(
            name="potassium",
            category="micro",
            subcategory="mineral",
            meassure_unit="mg",
        )

        self.testNutrient2 = Nutrient.objects.create(
            name="sodium",
            category="micro",
            subcategory="mineral",
            meassure_unit="mg",
        )

        self.testNutrient3 = Nutrient.objects.create(
            name="calcium",
            category="micro",
            subcategory="mineral",
            meassure_unit="mg",
        )

    def test_nutrient_access_will_work(self):
        """check if nutrients can be created and maybe contain some values"""
        testing_nutrients = Nutrient.objects.all()
        self.assertEqual(testing_nutrients.count(), 3)
        self.assertEqual(self.testNutrient1.name, "potassium")
        self.assertEqual(self.testNutrient2.name, "sodium")
        self.assertEqual(self.testNutrient3.name, "calcium")
        self.assertEqual(self.testNutrient1.category, "micro")
        self.assertEqual(self.testNutrient2.category, "micro")
        self.assertEqual(self.testNutrient3.category, "micro")
        self.assertEqual(self.testNutrient1.subcategory, "mineral")
        self.assertEqual(self.testNutrient2.subcategory, "mineral")
        self.assertEqual(self.testNutrient3.subcategory, "mineral")
        self.assertEqual(self.testNutrient1.meassure_unit, "mg")
        self.assertEqual(self.testNutrient2.meassure_unit, "mg")
        self.assertEqual(self.testNutrient3.meassure_unit, "mg")

    def test_nutrient_access_wont_work(self):
        """check if access to ingredients will fail"""
        testing_nutrients = Nutrient.objects.all()
        for nutrient in testing_nutrients:
            self.assertNotEqual(nutrient.name, "sugar")
            self.assertNotEqual(nutrient.category, "macro")
            self.assertNotEqual(nutrient.subcategory, "carbs")
            self.assertNotEqual(nutrient.meassure_unit, "µg")
