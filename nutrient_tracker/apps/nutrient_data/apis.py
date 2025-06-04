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


class NutrientList(APIView):
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

    def get(self, request, format=None):
        nutrients = Nutrient.objects.all()
        serializer = NutrientSerializer(nutrients, many=True)
        return Response(serializer.data)


class NutrientDetail(APIView):
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

    def get_object(self, pk):
        try:
            return Nutrient.objects.get(pk=pk)
        except Nutrient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nutrient = self.get_object(pk)
        serializer = NutrientSerializer(nutrient)
        return Response(serializer.data)
