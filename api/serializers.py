from rest_framework import serializers

from .models import Product, Primary


class PrimarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Primary
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


