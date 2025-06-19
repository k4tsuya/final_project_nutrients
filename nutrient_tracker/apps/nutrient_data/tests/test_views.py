from django.test import TestCase
from django.urls import reverse
from apps.nutrient_data.views import nutrient_list, nutrient_detail


# Create your tests here.
class NutrientViewsTest(TestCase):
    def test_nutrient_list_view(self):
        url = reverse("nutrient_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nutrient_list.html")

    def test_nutrient_detail_view(self):
        url = reverse("nutrient_detail", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nutrient_detail.html")
