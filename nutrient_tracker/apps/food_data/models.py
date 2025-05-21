from django.db import models
from apps.nutrient_data.models import Nutrient


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    estimated_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    nutrients = models.ManyToManyField(Nutrient)
    nutrition_value = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
