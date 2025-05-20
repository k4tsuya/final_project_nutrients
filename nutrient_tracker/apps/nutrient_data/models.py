"""Django REST Framework models for nutrient data."""

from django.db import models
from apps.nutrient_data.enums import Category, Subcategory

# Create your models here.

from rest_framework import serializers


# Create your models here.
class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    # is_micronutrient determines if its macro or micro nutrients
    category = models.CharField(  # macro, micro
        max_length=100,
        choices=Category.get_choices(),
        default=Category.get_default_category(),
    )
    subcategory = models.CharField(  # vitamin, mineral, carbs, etc.
        max_length=100,
        choices=Subcategory.get_choices(),
        default=Subcategory.get_default_subcategory(),
    )
    meassure_unit = models.CharField(max_length=2)  # g, mg, µg

    class Meta:
        verbose_name = "Nutrient"
        verbose_name_plural = "Nutrients"


# Serializers
class NutrientSerializer(serializers.ModelSerializer):
    """Serializer for nutrient data."""


# turn this into a rest API
# add categories for the different forms of nutrients
# add nutrient value from given databank
