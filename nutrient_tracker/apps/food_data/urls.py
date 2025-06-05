from django.urls import path, include
from apps.food_data import apis


urlpatterns = [
    path("list/", apis.IngredientView.as_view()),
    path("ingredient/", apis.IngredientSearchNameDetail.as_view()),
    path("category/", apis.IngredientCategoryDetail.as_view()),
    path("nutrient/", apis.IngredientNutrientValue.as_view()),
]
