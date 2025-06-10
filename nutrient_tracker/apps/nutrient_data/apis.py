import json
from pathlib import Path

from apps.user_info.models import User
from apps.user_info.serializers import UserSerializer
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from apps.nutrient_data.models import Nutrient
from apps.nutrient_data.serializers import NutrientSerializer
from rest_framework import filters, generics, status
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination


class NutrientList(generics.ListAPIView):
    serializer_class = NutrientSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    queryset = Nutrient.objects.order_by("pk")


class NutrientDetail(generics.ListAPIView):
    serializer_class = NutrientSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Nutrient.objects.none()

    def get_object(self, pk):
        try:
            return Nutrient.objects.get(pk=pk)
        except Nutrient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nutrient = self.get_object(pk=pk)
        serializer = NutrientSerializer(nutrient)
        return Response(serializer.data)
