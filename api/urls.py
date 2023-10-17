from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet, PrimaryViewSet

router = routers.DefaultRouter()
router.register("primary", PrimaryViewSet)
router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]
