from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Role, RoleSerializer
from api_back.pagination import CustomPagination


class RoleViewSet( viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    #pagination_class = CustomPagination
