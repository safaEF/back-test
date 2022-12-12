from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistoricalSerializer, Historical
from api_back.permissions import CustomDjangoModelPermissions



# Create your views here.

class GetHistoricalViewSet(viewsets.ModelViewSet):
    queryset = Historical.objects.all()
    serializer_class = HistoricalSerializer
    # pagination_class = CustomPagination
    permission_classes = (CustomDjangoModelPermissions,)
    http_method_names = ['get']