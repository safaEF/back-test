from django.shortcuts import render
from rest_framework import viewsets
from .pagination import CustomPagination
from .serializers import UserProfileSerializer, PermissionSerializer, GroupSerializer
from django.contrib.auth.models import User, Permission, Group
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from datetime import datetime
from django.conf import settings
import jwt
from role.models import token
#from django.contrib.auth.mixins import 


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    token_object = token(user=user, user_token=encoded_jwt)
    token_object.save()

    return encoded_jwt.decode('utf-8')

@api_view(['POST'])
def login(request):

    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')
    response = Response()
    user.user_permissions.set(user.groups.all()[0].permissions.all())
    # print(user,user.groups.get(name='patient').permissions.all())
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True, samesite='none', secure=True)
    response.data = {
        'jwt': token,
        'type': user.groups.all()[0].name
    }
    return response

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

