from django.urls import path, include
from apps.tracker_data import apis


urlpatterns = [
    path("trackers/", apis.IngredientView.as_view()),
    path("trackers/<int:pk>/", apis.IngredientDetail.as_view()),
]
