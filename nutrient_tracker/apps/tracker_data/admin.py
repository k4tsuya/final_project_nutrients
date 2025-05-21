from django.contrib import admin
from apps.tracker_data.models import NutrientTracker, NutrientRange

# Register your models here.
admin.site.register(NutrientTracker)
admin.site.register(NutrientRange)
