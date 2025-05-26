from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view
from apps.food_data.serializers import (
    IngredientDataSerializer,
)
from pathlib import Path
import json
from apps.food_data.models import Ingredient
from rest_framework import status
from django.http import JsonResponse


class IngredientView(APIView):
    serializer_class = IngredientDataSerializer

    def get(self, request):
        nutrients = Ingredient.objects.all()
        serializer = self.serializer_class(nutrients, many=True)
        return Response(serializer.data)

    def post(self, request, *args):
        return Response()
