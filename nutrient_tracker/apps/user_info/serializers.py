from rest_framework import serializers
from .models import Favorite, History, User, TrackedNutrients


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class TrackedNutrientsSerializer(serializers.ModelSerializer):
    #needs adjustment to include the linked nutrient tracker
    class Meta:
        model = TrackedNutrients
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
