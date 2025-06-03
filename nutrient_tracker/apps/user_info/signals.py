from django.db.models.signals import request_finished, post_delete
from django.dispatch import receiver

from apps.user_info.models import User, Favorite, History
from apps.nutrient_data.models import IngredientList
from apps.food_data.models import Ingredient, Recipe

# send a signal for when an action is performed

# style:

# @receiver(signal_flag, sender=NameOfModel)
# def action_performed(sender, instance, created, **kwargs):
#     additional logic


# add entry to user favorite when button is clicked on recipe, ingredient or nutrient

# remove entry to user favorite when button is clicked on recipe, ingredient or nutrient
