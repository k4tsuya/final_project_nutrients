import django_filters
from .models import Ingredient
from django_filters import rest_framework as filter


class IngredientFilter(django_filters.FilterSet):
    food_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Ingredient
        fields = ["food_name"]


class CategoryFilter(django_filters.FilterSet):
    food_group = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Ingredient
        fields = ["food_group"]
