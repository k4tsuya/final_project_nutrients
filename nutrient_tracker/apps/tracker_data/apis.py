import json
from pathlib import Path

from apps.tracker_data.models import NutrientTracker
from apps.tracker_data.serializers import NutrientTrackerSerializer
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tracker_data.models import NutrientTracker


class IngredientView(APIView):
    def get(self, request, format=None):
        ingredients = NutrientTracker.objects.all()
        serializer = NutrientTrackerSerializer(ingredients, many=True)
        return Response(serializer.data)


class IngredientDetail(APIView):
    def get_object(self, pk):
        try:
            return NutrientTracker.objects.get(pk=pk)
        except NutrientTracker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nutrient_tracker = self.get_object(pk)
        serializer = NutrientTrackerSerializer(nutrient_tracker)
        return Response(serializer.data)
