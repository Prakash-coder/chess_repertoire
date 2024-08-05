# serializers.py
from rest_framework import serializers
from .models import Opening, Variation

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['id', 'name', 'moves']

class OpeningSerializer(serializers.ModelSerializer):
    variations = VariationSerializer(many=True, read_only=True)

    class Meta:
        model = Opening
        fields = ['id', 'name', 'eco', 'moves', 'variations']
