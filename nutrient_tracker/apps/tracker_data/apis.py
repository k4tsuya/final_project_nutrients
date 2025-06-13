import json
from pathlib import Path

from apps.tracker_data.models import NutrientTracker
from apps.tracker_data.serializers import NutrientTrackerSerializer
from django.db import models
from django.db.models import QuerySet
from django.http import Http404, JsonResponse
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class NutrientTrackerList(generics.ListAPIView):
    """List all nutrient trackers."""

    serializer_class = NutrientTrackerSerializer

    def get_permissions(self) -> list:
        """Return the list of permissions that this view requires."""
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self) -> QuerySet:
        """Return the list of nutrient trackers."""
        if getattr(self, "swagger_fake_view", False):
            return NutrientTracker.objects.none()
        return None

    def get(self, request, format=None):
        ingredients = NutrientTracker.objects.all()
        serializer = NutrientTrackerSerializer(ingredients, many=True)
        return Response(serializer.data)


class NutrientTrackerDetail(generics.ListAPIView):
    """Retrieve a single nutrient tracker."""

    serializer_class = NutrientTrackerSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return NutrientTracker.objects.none()

    def get_object(self, pk):
        try:
            return NutrientTracker.objects.get(pk=pk)
        except NutrientTracker.DoesNotExist:
            raise Http404

    @extend_schema(
        operation_id="get_nutrient_tracker",
        summary="Retrieve a single nutrient tracker",
    )
    def get(self, request, pk, format=None):
        nutrient_tracker = self.get_object(pk)
        serializer = NutrientTrackerSerializer(nutrient_tracker)
        return Response(serializer.data)
