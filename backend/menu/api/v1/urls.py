from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    ItemViewSet,
    CategoryViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("itemvariant", ItemVariantViewSet)
router.register("review", ReviewViewSet)
router.register("category", CategoryViewSet)
router.register("country", CountryViewSet)
router.register("item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
