from django.contrib import admin
from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
