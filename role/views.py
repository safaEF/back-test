from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Role, RoleSerializer
from api_back.pagination import CustomPagination
from django.contrib.auth.mixins import PermissionRequiredMixin


class RoleViewSet( viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    #pagination_class = CustomPagination
    #permission_required = ('role.view_role', 'role.create_role', 'role.change_role', 'role.delete_role')
