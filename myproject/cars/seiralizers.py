from rest_framework import serializers
from .models import *


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['title', 'cars_name', 'description', 'marka', 'price',
                  'color', 'volume', 'year', 'type_change', 'video', 'image']