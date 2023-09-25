from rest_framework import viewsets, permissions, authentication

from .models import Packing1, Packing2, Packing3, Product
from .serializers import ProductSerializer, Packing1Serializer, Packing2Serializer, Packing3Serializer


class Packing1ViewSet(viewsets.ModelViewSet):
    queryset = Packing1.objects.all()
    serializer_class = Packing1Serializer


class Packing2ViewSet(viewsets.ModelViewSet):
    queryset = Packing2.objects.all()
    serializer_class = Packing2Serializer


class Packing3ViewSet(viewsets.ModelViewSet):
    queryset = Packing3.objects.all()
    serializer_class = Packing3Serializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]
