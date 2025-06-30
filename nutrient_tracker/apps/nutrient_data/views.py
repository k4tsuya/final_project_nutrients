from django.shortcuts import render, get_object_or_404
from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Nutrient
from scripts.utils import limit_m2m_field

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


def nutrient_list(request):
    nutrients = Nutrient.objects.all()
    return render(request, "nutrient_list.html", {"nutrients": nutrients})


def nutrient_detail(request, pk):
    nutrient = get_object_or_404(Nutrient, pk=pk)
    if request.user.is_authenticated:
        limit_m2m_field(request.user.history.nutrient)
        request.user.history.nutrient.add(nutrient)
    return render(request, "nutrient_detail.html", {"nutrient": nutrient})


# to grab the measurement unit from the nutrient
# write {{ nutrient.measurement_unit }} inside the template
# as the content either refers to nutrients or nutrient
# depending on if you use the singular or plural form
