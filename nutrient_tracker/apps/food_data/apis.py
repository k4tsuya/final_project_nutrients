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


class IngredientView(APIView):
    serializer_class = IngredientDataSerializer

    def get(self, request):
        nutrients = Ingredient.objects.all()
        serializer = self.serializer_class(nutrients, many=True)
        return Response(serializer.data)

    def post(self, request, *args):
        return Response()


class IngredientSearchNameDetail(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDataSerializer
    filterset_class = IngredientFilter


class IngredientCategoryDetail(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDataSerializer
    filterset_class = CategoryFilter
