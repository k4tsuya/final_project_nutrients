from apps.food_data.models import Ingredient, Recipe
from apps.nutrient_data.models import Nutrient
from apps.tracker_data.models import NutrientTracker
from apps.user_info.enums import Gender, Role
from django.contrib.auth.models import AbstractUser
from django.db import models


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
    # grab associated nutrient_trackers for frontend a different way

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super().save(force_insert, force_update, *args, **kwargs)

        print("User primary key:", self.pk)
        if not self.pk:
            tracked_nutrients = TrackedNutrients.objects.create(
                user=self, nutrient_tracker=None
            )
            tracked_nutrients.save()
            favourites = Favorite.objects.create(user=self)
            favourites.save()
            history = History.objects.create(user=self)
            history.save()
        super().save(force_insert, force_update, *args, **kwargs)

    def __str__(self) -> str:
        """Return the string representation of the user."""
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=False,
    )
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
        return f"{self.user.username}'s Favorite List"


class History(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
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
        return f"{self.user.username}'s History List"


class TrackedNutrients(models.Model):
    # foreignkey because a user can only have one tracked nutrient table
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # many to one because a user can have many nutrient_trackers
    # try with many to many to see if it works and compresses
    nutrient_tracker = models.ForeignKey(
        NutrientTracker, on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = "Tracked Nutrient"
        verbose_name_plural = "Tracked Nutrients"

    def __str__(self):
        return f"{self.user.username}'s tracked nutrients"
