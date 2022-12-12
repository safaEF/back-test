from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from historical.models import Historical

from product.models import Product
from django.dispatch import receiver



# post_save method
@receiver(post_save, sender=Product) 
def create_product(sender, instance, created, **kwargs):
    print("sender", sender)
    print("instance", instance)
    print("created", created)
    Historical.objects.create(model="Product", action="Post")




# post_delete method
@receiver(post_delete,sender=Product)
def delete_product(sender,instance,*args,**kwargs):
    Historical.objects.create(model="Product", action="delete")
    print("Product Deleted")
