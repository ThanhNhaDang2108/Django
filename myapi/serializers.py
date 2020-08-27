# serializers.py
from rest_framework import serializers
from django.http import JsonResponse
from .models import ThanhNha, Recipe

class ThanhNhaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThanhNha
        fields = ('id', 'name', 'alias')
# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Recipe
#         fields = ('name', 'amount', 'measurement')

class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('slug', 'name', 'description', 'cooking_instructions',
            'cooking_time', 'preparation_time',
            'created', 'modified')