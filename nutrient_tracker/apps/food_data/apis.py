"""API for retrieving ingredient data."""

from typing import ClassVar

import django_filters.rest_framework
from apps.food_data.models import Ingredient
from apps.food_data.serializers import (
    IngredientDataSerializer,
)
from django.db import models
from django.db.models import QuerySet
from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from .filters import CategoryFilter, IngredientFilter
from drf_spectacular.utils import extend_schema


class IngredientView(generics.ListAPIView):
    """Ingredient data view."""

    throttle_classes: ClassVar[list] = [UserRateThrottle, AnonRateThrottle]
    queryset: ClassVar[models.QuerySet] = Ingredient.objects.order_by("pk")
    serializer_class = IngredientDataSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_permissions(self) -> list:
        """Return the list of permissions that this view requires."""
        self.permission_classes = [AllowAny]
        if self.request.method in {"POST", "PUT", "DELETE", "PATCH", "UPDATE"}:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientSearchNameDetail(generics.ListAPIView):
    """Return a list of the ingredients by name."""

    serializer_class = IngredientDataSerializer
    throttle_classes: ClassVar[list] = [UserRateThrottle, AnonRateThrottle]

    queryset: ClassVar[models.QuerySet] = Ingredient.objects.order_by("pk")
    filterset_class = IngredientFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_permissions(self) -> list:
        """Return the list of permissions that this view requires."""
        self.permission_classes = [AllowAny]
        if self.request.method in {"POST", "PUT", "DELETE", "PATCH", "UPDATE"}:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientCategoryDetail(generics.ListAPIView):
    """Return a list of the ingredients by category."""

    serializer_class = IngredientDataSerializer
    throttle_classes: ClassVar[list] = [UserRateThrottle, AnonRateThrottle]
    filterset_class = CategoryFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    queryset = Ingredient.objects.order_by("pk")

    def get_permissions(self) -> list:
        """Return the list of permissions that this view requires."""
        self.permission_classes = [AllowAny]
        if self.request.method in {"POST", "PUT", "DELETE", "PATCH", "UPDATE"}:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientNutrientValue(generics.ListAPIView):
    """Return a list of the nutrients by ingredient."""

    serializer_class = IngredientDataSerializer
    throttle_classes: ClassVar[list] = [UserRateThrottle, AnonRateThrottle]

    filterset_backends: ClassVar[list] = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filter_backends: ClassVar[list] = [DjangoFilterBackend]
    ordering_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    abbreviation = {
        "enercj": "kj",
        "enercc": "kcal",
        "water": "water",
        "protein": "prot",
        "calcium": "ca",
        "iron": "fe",
        "potassium": "k",
        "sodium": "na",
    }

    def abbreviation_filter(self, query):
        for key, value in self.abbreviation.items():
            if query in key:
                return value
        return query

    def get_queryset(self) -> QuerySet:
        """Return the queryset."""
        query = self.request.query_params.get("search")
        if getattr(self, "swagger_fake_view", False):
            return Ingredient.objects.none()
        try:
            # filter_by_nutrient = Ingredient.objects.order_by(
            #     "-" + self.abbreviation[query]
            # )
            filter_by_nutrient = Ingredient.objects.order_by(
                "-" + self.abbreviation_filter(query)
            )
            return filter_by_nutrient
        except:
            raise Http404
