from django.urls import path, include
from apps.nutrient_data import apis


urlpatterns = [
    path("nutrients/", apis.NutrientList.as_view()),
]
