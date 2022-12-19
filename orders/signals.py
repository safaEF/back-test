from django.db.models.signals import post_save, pre_save, post_delete
from historical.models import Historical

from .models import Order
from django.forms.models import model_to_dict
from django.dispatch import receiver



# pre_save method
@receiver(pre_save, sender=Order) 
def update_Order(sender, instance, **kwargs):
    if instance.id:
        obj = Order.objects.get(id=instance.id)
        fields = model_to_dict(obj)
        print("test",fields)
        for field in fields:
            if getattr(obj,field) != getattr(instance,field):
                print('fields', field)
                print('obj', obj)
                print('instance', instance)
                print('fields', fields)
                Historical.objects.create(model="Order", action="Put", pre=getattr(obj,field), post=getattr(instance,field), field_updated=field)



# post_save method
@receiver(post_save, sender=Order) 
def create_Order(sender, instance, created, **kwargs):
    if created:
        print('Done created')
        Historical.objects.create(model="Order", action="Post")
         
""" @receiver(pre_save, sender=Order) 
def pre_update_Order(sender, instance, **kwargs):
    if instance.id:
        if Order.objects.get(id=instance.id):
            pd = Order.objects.get(id=instance.id)
            print('Done pre update', pd.title)
            print('Done post update', instance.title)
            Historical.objects.create(model="Order", action="Put", pre= pd.)
    """
# post_delete method
@receiver(post_delete,sender=Order)
def delete_Order(sender,instance,*args,**kwargs):
    Historical.objects.create(model="Order", action="delete")
    print("Order Deleted")
