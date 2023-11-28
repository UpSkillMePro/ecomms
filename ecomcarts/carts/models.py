from django.db import models


# Create your models here.
class Cart(models.Model):
    title = models.CharField(max_length=200)
    user = models.BigIntegerField()


class Items(models.Model):
    product = models.BigIntegerField()
    quantity = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)