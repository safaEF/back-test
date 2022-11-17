from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return "%s" % (self.title)