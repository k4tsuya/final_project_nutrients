"""Django REST Framework models for nutrient data."""

from django.db import models
from apps.nutrient_data.enums import Category, Subcategory


# Create your models here.
class Nutrient(models.Model):
    nutrient_name = models.CharField(max_length=100, unique=True, blank=False)
    measure_unit = models.CharField(max_length=4)  # g, mg, µg

    class Meta:
        verbose_name = "Nutrient"
        verbose_name_plural = "Nutrients"

    def __str__(self):
        return self.nutrient_name
