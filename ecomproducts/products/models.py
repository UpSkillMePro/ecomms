from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.TextField()
