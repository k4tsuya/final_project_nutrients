from apps.food_data.models import Ingredient, Recipe
from apps.nutrient_data.models import Nutrient
from apps.user_info.enums import Gender, Role
from django.contrib.auth.models import AbstractUser
from django.db import models


class Favorite(models.Model):
    nutrient = models.ManyToManyField(
        Nutrient,
    )
    ingredient = models.ManyToManyField(
        Ingredient,
    )
    recipe = models.ManyToManyField(
        Recipe,
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self) -> str:
        """Return the string representation of the favorite list."""
        return "Favorite List"


class History(models.Model):
    nutrient = models.ManyToManyField(
        Nutrient,
        max_length=10,
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        max_length=10,
    )
    recipe = models.ManyToManyField(
        Recipe,
        max_length=10,
    )

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"

    def __str__(self) -> str:
        """Return the string representation of the favorite list."""
        return "History List"


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
    username = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
    )
    # Gender.male,female,others
    gender = models.CharField(
        max_length=10,
        choices=Gender.get_gender(),
        default=Gender.get_default_gender(),
    )
    # nutrient_tracker = models.ManyToManyField(NutrientTracker, blank=True)
    # maybe grab associated nutrient_trackers for frontend a different way
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    history = models.ForeignKey(
        History,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        print("User primary key:", self.pk)
        if not self.pk:
            if self.favorite is None:
                self.favorite = Favorite.objects.create()
            if self.history is None:
                self.history = History.objects.create()
        super().save(force_insert, force_update, *args, **kwargs)
        # if self.pk:
        #     if self.nutrient_tracker is None:
        #         nutrients = Nutrient.objects.all()
        #         self.nutrient_tracker = NutrientTracker.objects.bulk_create(
        #             [
        #                 NutrientTracker(date=self.date_joined, nutrient_range=nutrient)
        #                 for nutrient in nutrients
        #             ]
        #         )
        # super().save(force_insert, force_update, *args, **kwargs)
        print("User saved:", self.pk)

    def __str__(self) -> str:
        """Return the string representation of the user."""
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

