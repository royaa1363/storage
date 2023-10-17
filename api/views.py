from rest_framework import viewsets, permissions, authentication

from .models import Product, Primary
from .serializers import ProductSerializer, PrimarySerializer


class PrimaryViewSet(viewsets.ModelViewSet):
    queryset = Primary.objects.all()
    serializer_class = PrimarySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]
