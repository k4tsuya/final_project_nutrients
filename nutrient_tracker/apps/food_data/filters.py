import django_filters
from .models import Ingredient


class IngredientFilter(django_filters.FilterSet):
    class Meta:
        model = Ingredient
        fields = {
            "food_name": ["icontains", "iexact"],
        }


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Ingredient
        fields = {
            "food_group": ["icontains", "iexact"],
        }
