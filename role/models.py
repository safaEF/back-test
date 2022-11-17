from django.db import models
from django.contrib.auth.models import Permission, User


class Role(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    permissions=models.ManyToManyField(Permission, related_name="PermissionData")

    def __str__(self):
        return "%s" % (self.name)


class token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_token = models.CharField(max_length=200)

    def __str__(self):
        return self.user_token
