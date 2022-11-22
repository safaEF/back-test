from django.contrib import admin
from .models import Order, OrderItem
from django.contrib.auth.models import Permission


# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Permission)

