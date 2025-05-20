"""Django REST Framework models for nutrient data."""

from rest_framework import serializers

# Create your models here.


# Serializers
class NutrientSerializer(serializers.ModelSerializer):
    """Serializer for nutrient data."""
