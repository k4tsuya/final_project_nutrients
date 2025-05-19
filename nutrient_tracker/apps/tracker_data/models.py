from django.db import models
from apps.nutrient_data.models import Nutrient

# Create your models here.


class NutrientRange(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    min = models.FloatField()
    max = models.FloatField()
    current_value = models.FloatField()

    class Meta:
        verbose_name = "Nutrient Range"
        verbose_name_plural = "Nutrient Ranges"


class NutrientTracker(models.Model):
    date = models.DateField()
    nutrient_range = models.ManyToManyField(NutrientRange)

    def __str__(self):
        return f"{self.user} - {self.date}"

    class Meta:
        verbose_name = "Nutrient Tracker"
        verbose_name_plural = "Nutrient Trackers"


# compare nutrient ranges
# compare intake to current value and ranges
