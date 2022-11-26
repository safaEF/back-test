import csv
from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderItemSerializer, Order, OrderItem

from api_back.pagination import CustomPagination
from django.http import HttpResponse
from rest_framework.response import Response
from api_back.permissions import CustomDjangoModelPermissions


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = CustomPagination
    permission_classes = (CustomDjangoModelPermissions,)



class GetOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    http_method_names = ['get']
    permission_classes = (CustomDjangoModelPermissions,)


class PostOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    http_method_names = ['post']
    permission_classes = (CustomDjangoModelPermissions,)


class PutOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    http_method_names = ['put']
    permission_classes = (CustomDjangoModelPermissions,)


class DeleteOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    http_method_names = ['delete']
    permission_classes = (CustomDjangoModelPermissions,)



class ExportAPIView(APIView):
    def get(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachement; filename=orders.csv'

        orders = Order.objects.all()
        writer = csv.writer(response)

        writer.writerow(['ID', 'Name', 'Email', 'Product Title', 'Price', 'Quantity'])
        for order in orders:
            ordersitems = OrderItem.objects.all().filter(id=order.id)
            for item in ordersitems:
                writer.writerow([order.id, order.name, order.email,item.product_title, item.price, item.quantity])
        return  response


class ChartAPIView(APIView):
    def get(self, _):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT sum(i.quantity * i.price) as sum
            from orders_order as o 
            JOIN orders_orderitem as i 
            ON o.id = i.id 
        
            """)
            row = cursor.fetchall()

            return Response({
                'data': row
            })