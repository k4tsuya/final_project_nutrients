from django.urls import path, include
from apps.tracker_data import apis


urlpatterns = [
    path("trackers/", apis.NutrientTrackerList.as_view()),
    path("trackers/<int:pk>/", apis.NutrientTrackerDetail.as_view()),
]
