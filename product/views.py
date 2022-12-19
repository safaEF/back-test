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

class FileUploadView(APIView):
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):

      file_serializer = ProductSerializer(data=request.data)

      if file_serializer.is_valid():

        file = request.FILES['image']
        file_serializer.save()
        url = default_storage.url(file)
        return Response({"url": 'http://127.0.0.1:8000'+url, "data":file_serializer.data},  status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)