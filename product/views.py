from django.shortcuts import render
from .serializers import ProductSerializer, Product
from api_back.pagination import CustomPagination
from rest_framework import viewsets
from django.contrib.auth.mixins import PermissionRequiredMixin



class GetProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = CustomPagination
    http_method_names = ['get']
    # permission_required = ('product.view_product')


class PostProductViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = CustomPagination
    http_method_names = ['post']
    permission_required = ('product.add_product')


class PutProductViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = CustomPagination
    http_method_names = ['put']
    permission_required = ('product.change_product')


class DeleteProductViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = CustomPagination
    http_method_names = ['delete']
    permission_required = ('product.delete_product')
