from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ThanhNhaSerializer, RecipeSerializer
from .models import ThanhNha, Recipe
from . import serializers
class ThanhNhaViewSet(viewsets.ModelViewSet):
    queryset = ThanhNha.objects.all().order_by('name')
    serializer_class = ThanhNhaSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    # serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer