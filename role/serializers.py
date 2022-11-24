from rest_framework import serializers
from .models import Role
from api_back.serializers import PermissionSerializer

class RoleSerializer(serializers.ModelSerializer):
    # PermissionData = PermissionSerializer(source="permissions", many=True, read_only=True)
    permissions_list = PermissionSerializer(source="permissions", many=True, read_only=True)
    class Meta:
        model = Role
        fields = ('permissions_list',)