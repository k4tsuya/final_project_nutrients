from django.shortcuts import render, get_object_or_404
from apps.food_data.models import Ingredient, Recipe
from scripts.utils import limit_m2m_field
from rest_framework import generics, filters
from .models import Ingredient
from .serializers import IngredientSerializer


# Create your views here.

# class IngredientListView(generics.ListAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['food_name', 'food_group']


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user.is_authenticated:
        limit_m2m_field(request.user.history.recipe)
        request.user.history.recipe.add(recipe)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(
        request, "ingredient_list.html", {"ingredients": ingredients}
    )


def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.user.is_authenticated:
        limit_m2m_field(request.user.history.ingredient)
        request.user.history.ingredient.add(ingredient)
    return render(
        request, "ingredient_detail.html", {"ingredient": ingredient}
    )
