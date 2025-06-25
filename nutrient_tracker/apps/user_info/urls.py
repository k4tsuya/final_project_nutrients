from django.urls import path, include
from apps.user_info import apis, views


urlpatterns = [
    path("users/", apis.UserView.as_view(), name="users"),
    path("users/<int:pk>/", apis.UserDetailView.as_view(), name="user_detail"),
    path(
        "users/<int:pk>/history/",
        apis.UserHistoryView.as_view(),
        name="user_history",
    ),
    path(
        "users/<int:pk>/favorite/",
        apis.UserFavoriteView.as_view(),
        name="user_favorite",
    ),
    path(
        "users/<int:pk>/tracked_nutrients/",
        apis.TrackedNutrientsView.as_view(),
        name="user_tracked_nutrients",
    ),
]
