from django.db import models
from apps.nutrient_data.models import Nutrient


# Create your models here.


class NutrientRange(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.DO_NOTHING)
    min = models.FloatField()
    max = models.FloatField()
    current_value = models.FloatField()

    class Meta:
        verbose_name = "Nutrient Range"
        verbose_name_plural = "Nutrient Ranges"

    def __str__(self):
        return f"{self.nutrient.food_name}"


class NutrientTracker(models.Model):
    date = models.DateField()
    nutrient_range = models.ManyToManyField(NutrientRange)

    class Meta:
        verbose_name = "Nutrient Tracker"
        verbose_name_plural = "Nutrient Trackers"

    def __str__(self):
        return f"{self.date} - Nutrient Tracker"


# compare nutrient ranges
# compare intake to current value and ranges
