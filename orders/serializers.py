from rest_framework import serializers
from .models import Order, OrderItem
from django.db import models


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    OrderData = OrderItemSerializer(source="order", many=True, read_only=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        items = OrderItem.objects.all().filter(id = obj.id)
        return sum((o.price * o.quantity) for o in items)
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name',
                  'email', 'order', 'OrderData', 'total')

