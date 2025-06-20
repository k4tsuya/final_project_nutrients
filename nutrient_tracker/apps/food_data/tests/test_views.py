from django.test import TestCase
from django.urls import reverse

from apps.food_data.views import (
    ingredient_list,
    recipe_list,
    recipe_detail,
    ingredient_detail,
)


# Create your tests here.
class TestFoodData(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/api/v1/food/list/")
        self.assertEqual(response.status_code, 200)

    def test_ingredient_detail_works(self):
        response = self.client.get("/api/v1/food/ingredient/", args=[1])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_works(self):
        response = self.client.get(reverse("recipe_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe_list.html")

    def test_recipe_detail_works(self):
        response = self.client.get(reverse("recipe_detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe_detail.html")
