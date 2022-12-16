from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Historical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    pre = models.CharField(max_length=255, null=True, blank=True)
    post = models.CharField(max_length=255, null=True, blank=True)
    field_updated = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return "%s" % (self.user)