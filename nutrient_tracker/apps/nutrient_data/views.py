from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Nutrient
from ..food_data.serializers import NutrientDataSerializer
from django.db import transaction
# Create your views here.


# class NutrientBulkView(APIView):
#     def post(self, request):
#         serializer = NutrientDataSerializer(data=request, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, staus=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request):
#         data = request.data
#         with transaction.atomic():
#             for item in data:
