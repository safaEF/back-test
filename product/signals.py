from django.db.models.signals import post_save, pre_save, post_delete
from historical.models import Historical

from product.models import Product
from django.forms.models import model_to_dict
from django.dispatch import receiver


# pre_save method
@receiver(pre_save, sender=Product) 
def update_product(instance, **kwargs):
    if instance.id:
        Prod_obj = Product.objects.get(id=instance.id)
        fields = model_to_dict(Prod_obj)

        for field in fields:
            if getattr(Prod_obj, field) != getattr(instance, field):
                
                Historical.objects.create(model="Product", action="Put", pre=getattr(Prod_obj, field),
                                          post=getattr(instance, field), field_updated=field)


# post_save method
@receiver(post_save, sender=Product) 
def create_product(sender, instance, created, **kwargs):
    if created:
        print('Done create')
        Historical.objects.create(model="Product", action="Post")


# post_delete method
@receiver(post_delete, sender=Product)
def delete_product(sender, instance, *args, **kwargs):
    Historical.objects.create(model="Product", action="delete")
    print("Product Deleted")
