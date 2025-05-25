from django.db import models
from apps.nutrient_data.models import Nutrient
from apps.user_info.models import User
from django.utils import timezone

# Create your models here.


class NutrientTracker(models.Model):
    date = models.DateField(default=timezone.now())
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="nutrient_trackers"
    )
    nutrient = models.ForeignKey(Nutrient, on_delete=models.DO_NOTHING)
    min = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    max = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    current_value = models.DecimalField(
        default=0, decimal_places=2, max_digits=10
    )

    class Meta:
        verbose_name = "Nutrient Tracker"
        verbose_name_plural = "Nutrient Trackers"

    def __str__(self):
        return f"{self.date} - Nutrient Tracker"


# compare nutrient ranges
# compare intake to current value and ranges
