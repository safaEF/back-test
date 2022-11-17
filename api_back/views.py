from django.shortcuts import render
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserProfileSerializer, PermissionSerializer, GroupSerializer
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny)
    serializer_class = MyTokenObtainPairSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = PermissionSerializer
    http_method_names = ['get']
    # permission_required = ('auth.view_user')


class GetUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    # permission_required = ('user.view_user')


class PostUserViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('user.create_user') 


class PutUserViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['put']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('user.change_user')


class DeleteUserViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('user.delete_user')


class GetGroupViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('group.view_group')


class PostGroupViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['post']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('change_group')


class PutGroupViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['put']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('create_group')


class DeleteGroupViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination
    #required_groups = ['Admin']
    permission_required = ('delete_group')
