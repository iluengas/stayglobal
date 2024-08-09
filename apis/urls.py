# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductViewSet.as_view(), name='product-list'),
    path('products/<str:category>/', ProductViewSet.as_view(),
         name='product-category-list'),
]
