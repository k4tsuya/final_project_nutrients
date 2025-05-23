from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view
from apps.nutrient_data.serializers import NutrientDataSerializer
from pathlib import Path
import json
from apps.nutrient_data.models import Nutrient
from rest_framework import status
from django.http import JsonResponse


# with Path.open("apps/nutrient_data/data/nevo_nutrient_data.json") as data_file:
#     nutrient_data = json.load(data_file)


class NutrientList(APIView):
    def get(self, request, *args):
        return Response()

    def post(self, request, *args):
        return Response()
