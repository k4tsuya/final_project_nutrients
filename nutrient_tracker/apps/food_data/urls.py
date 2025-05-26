from django.urls import path, include
from apps.food_data import apis


urlpatterns = [
    path("food/", apis.IngredientView.as_view()),
    path("food/<int:pk>", apis.IngredientView.as_view()),
]
