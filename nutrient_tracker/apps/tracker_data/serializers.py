from rest_framework import serializers
from .models import NutrientTracker


class NutrientTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutrientTracker
        fields = "__all__"