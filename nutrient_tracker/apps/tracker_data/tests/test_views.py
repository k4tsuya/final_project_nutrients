from django.test import TestCase
from django.urls import reverse

from apps.tracker_data.views import NutrientTrackerListView


class NutrientTrackerListViewTest(TestCase):
    def test_nutrient_tracker_list_view(self):
        url = reverse("nutrient_tracker_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nutrient_tracker_list.html")