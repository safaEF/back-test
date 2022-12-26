from django.shortcuts import render
from .serializers import ProductSerializer, Product
from api_back.pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from api_back.permissions import CustomDjangoModelPermissions


class GetProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = CustomPagination
    permission_classes = (CustomDjangoModelPermissions,)
    http_method_names = ['get']


class PostProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = CustomPagination
    http_method_names = ['post']
    permission_classes = (CustomDjangoModelPermissions,)
 

class PutProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = CustomPagination
    http_method_names = ['patch']
    permission_classes = (CustomDjangoModelPermissions,)

class DeleteProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = CustomPagination
    http_method_names = ['delete']
    permission_classes = (CustomDjangoModelPermissions,)