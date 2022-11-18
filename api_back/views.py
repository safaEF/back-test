from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer, PermissionSerializer, GroupSerializer
from django.contrib.auth.models import User, Permission, Group

#from django.contrib.auth.mixins import 

class GetUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')

class PostUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['post']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user') 

class PutUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['put']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')

class DeleteUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')
    #     
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    #permission_required = ('permission.view_permission', 'permission.create_permission', 'permission.change_permission', 'permission.delete_permission')

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #pagination_class = CustomPagination
    #permission_required = ('group.view_group', 'group.create_group', 'group.change_group', 'group.delete_group')


class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')


class PostGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['post']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')


class PutGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['put']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')


class DeleteGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    #permission_required = ('user.view_user', 'user.create_user', 'user.change_user', 'user.delete_user')

