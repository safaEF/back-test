from django.db import models
from django.contrib.auth.models import Permission

class Role(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    permissions=models.ManyToManyField(Permission, related_name="PermissionData")

    def __str__(self):
        return "%s" % (self.name)
