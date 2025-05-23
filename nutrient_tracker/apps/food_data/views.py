from django.shortcuts import render, get_object_or_404
from apps.food_data.models import Ingredient, Recipe
from apps.nutrient_data.models import Nutrient


# Create your views here.
def limit_m2m_field(m2m_field, limit=10):
    current_items = list(m2m_field.all())
    if len(current_items) > limit:
        m2m_field.remove(current_items[0])
        m2m_field.save()


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


def nutrient_list(request):
    nutrients = Nutrient.objects.all()
    return render(request, "nutrient_list.html", {"nutrients": nutrients})


def nutrient_detail(request, pk):
    nutrient = get_object_or_404(Nutrient, pk=pk)
    if request.user.is_authenticated:
        limit_m2m_field(request.user.history.nutrient)
        request.user.history.nutrient.add(nutrient)
    return render(request, "nutrient_detail.html", {"nutrient": nutrient})
