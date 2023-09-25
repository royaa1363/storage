from rest_framework import serializers

from .models import Packing1, Packing2, Packing3, Product


class Packing1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Packing1
        fields = ['title']


class Packing2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Packing2
        fields = ['title']


class Packing3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Packing3
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'pro_num', 'pro_date', 'id']


