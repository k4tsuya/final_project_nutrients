from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user_info.enums import Role, Gender

from apps.nutrient_data.models import Nutrient
from apps.tracker_data.models import NutrientTracker
from apps.food_data.models import Ingredient, Recipe


# Create your models here.
class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=Role.get_roles(),
        default=Role.get_default_role(),
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    # PW needs hashing for security
    password = models.CharField(max_length=128, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    # Gender.male,female,others
    gender = models.CharField(
        max_length=10,
        choices=Gender.get_gender(),
        default=Gender.get_default_gender(),
    )
    nutrient_tracker = models.ManyToManyField(NutrientTracker)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite")
    nutrient = models.ManyToManyField(Nutrient)
    ingredient = models.ManyToManyField(Ingredient)
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return f"{self.user} - Favourite List"

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    nutrient = models.ManyToManyField(Nutrient, max_length=10)
    ingredient = models.ManyToManyField(Ingredient, max_length=10)
    recipe = models.ManyToManyField(Recipe, max_length=10)

    def __str__(self):
        return f"{self.user} - Favourite List"

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
