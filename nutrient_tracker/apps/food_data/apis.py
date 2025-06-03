import json
from pathlib import Path

from apps.food_data.models import Ingredient
from apps.food_data.serializers import (
    IngredientDataSerializer,
)
from django.http import Http404, JsonResponse
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import IngredientFilter, CategoryFilter
from rest_framework.pagination import PageNumberPagination


class IngredientView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDataSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5


class IngredientSearchNameDetail(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDataSerializer
    filterset_class = IngredientFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5


class IngredientCategoryDetail(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDataSerializer
    filterset_class = CategoryFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
