import django_filters.rest_framework
from apps.food_data.models import Ingredient
from apps.food_data.serializers import (
    IngredientDataSerializer,
)
from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .filters import IngredientFilter, CategoryFilter


class IngredientView(generics.ListAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = Ingredient.objects.order_by("pk")
    serializer_class = IngredientDataSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PATCH":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "UPDATE":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientSearchNameDetail(generics.ListAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    queryset = Ingredient.objects.order_by("pk")
    serializer_class = IngredientDataSerializer
    filterset_class = IngredientFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PATCH":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "UPDATE":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientCategoryDetail(generics.ListAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    queryset = Ingredient.objects.order_by("pk")
    serializer_class = IngredientDataSerializer
    filterset_class = CategoryFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "PATCH":
            self.permission_classes = [IsAdminUser]
        elif self.request.method == "UPDATE":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IngredientNutrientValue(generics.ListAPIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    serializer_class = IngredientDataSerializer
    filterset_backends = [django_filters.rest_framework.DjangoFilterBackend]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    filter_backends = [DjangoFilterBackend]
    ordering_fields = "__all__"

    def get_queryset(self):
        query = self.request.query_params.get("search")
        if getattr(self, "swagger_fake_view", False):
            return Ingredient.objects.none()
        try:
            filter_by_nutrient = Ingredient.objects.order_by("-" + query)
            return filter_by_nutrient
        except:
            raise Http404
