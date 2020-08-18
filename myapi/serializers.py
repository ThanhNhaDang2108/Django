# serializers.py
from rest_framework import serializers

from .models import ThanhNha

class ThanhNhaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThanhNha
        fields = ('id', 'name', 'alias')