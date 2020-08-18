from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ThanhNhaSerializer
from .models import ThanhNha


class ThanhNhaViewSet(viewsets.ModelViewSet):
    queryset = ThanhNha.objects.all().order_by('name')
    serializer_class = ThanhNhaSerializer