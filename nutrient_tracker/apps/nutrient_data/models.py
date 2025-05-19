from django.db import models

# Create your models here.


class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    # is_micronutrient determines if its macro or micro nutrients
    is_micronutrient = models.BooleanField(default=False)
    meassure_unit = models.CharField(max_length=2)  # g, mg, µg

    class Meta:
        verbose_name = "Nutrient"
        verbose_name_plural = "Nutrients"

    def __str__(self):
        return self.name

# turn this into a rest API
# add categories for the different forms of nutrients
# add nutrient value from given databank
