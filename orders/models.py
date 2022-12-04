from django.db import models
from django.db.models.signals import post_save



class OrderItem(models.Model):
    product_title = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.product_title)

    def create_orderitem(sender, instance, created, **kwargs):

        if created: 
            OrderItem.objects.create(product_title=instance)
            print('OrderItem created!')
    post_save.connect(create_orderitem, sender=product_title)
        # print('print this ')
        # print(instance.product_title)
        # print(instance.price)
        # print(instance.quantity)
        # pre_save.connect(create_orderitem, sender=OrderItem)


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

    
