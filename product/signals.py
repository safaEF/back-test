from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from historical.models import Historical

from product.models import Product
from django.dispatch import receiver


# pre_save method
@receiver(pre_save, sender=User) 
def create_product(sender, instance, created, **kwargs):
    Prod_obj = Product.objects.get(instance.title)
    fields = [Product]
    for i in fields:
        if Prod_obj.fields[i] != instance.fields[i]:
            create_product(fields(i), Prod_obj, fields)


    Historical.objects.create(model="Product", action="Post")



# post_save method
@receiver(post_save, sender=Product) 
def create_product(sender, instance, created, **kwargs):
    Historical.objects.create(model="Product", action="Post")


# post_delete method
@receiver(post_delete,sender=Product)
def delete_product(sender,instance,*args,**kwargs):
    Historical.objects.create(model="Product", action="delete")
    print("Product Deleted")
