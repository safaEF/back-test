from django.db import models


class OrderItem(models.Model):
    product_title = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.product_title)


class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.ManyToManyField(OrderItem, related_name="OrderData")


    def __str__(self):
        return "%s" % (self.first_name)

    @property
    def name(self):
        return self.first_name + '' + self.last_name
