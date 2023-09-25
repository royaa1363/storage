from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet, Packing1ViewSet, Packing2ViewSet, Packing3ViewSet

router = routers.DefaultRouter()
router.register("packing1", Packing1ViewSet)
router.register("packing2", Packing2ViewSet)
router.register("packing3", Packing3ViewSet)
router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]
