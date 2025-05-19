from django.contrib import admin
from apps.food_data.models import Ingredient, Recipe

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Recipe)
