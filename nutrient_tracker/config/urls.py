"""
URL configuration for nutrient_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from apps.tracker_data.views import NutrientTrackerListView
from apps.user_info.views import (
    HomeView,
    ProfileView,
    about_view,
    contact_view,
    login_view,
    logout_view,
    register_view,
    ingredients_view,
    nutrients_view,
    recipes_view,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


doc_urls = [
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

api_urls = [
    path("food/", include("apps.food_data.urls")),
    path("nutrient/", include("apps.nutrient_data.urls")),
    path("tracker/", include("apps.tracker_data.urls")),
    path("user/", include("apps.user_info.urls")),
]

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include(doc_urls)),
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls)),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path(
        "tracker/",
        NutrientTrackerListView.as_view(),
        name="tracker_pagination",
    ),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path(
        "tracker/",
        NutrientTrackerListView.as_view(),
        name="tracker_pagination",
    ),
    path("contact/", contact_view, name="contact"),
    path("about/", about_view, name="about"),
    path("ingredients/", ingredients_view, name="ingredients"),
    path("nutrients/", nutrients_view, name="nutrients"),
    path("recipes/", recipes_view, name="recipes"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
