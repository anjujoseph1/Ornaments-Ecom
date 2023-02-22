from django.db import models
from ornaments_app .models import *
# Create your models here.

class CartList(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date=models.DateTimeField(auto_now_add=True)

class CartItems(models.Model):
    prot=models.ForeignKey(Products,on_delete=models.CASCADE)
    cartli=models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class cartlist(models.Model):
    prot=models.ForeignKey(Products,on_delete=models.CASCADE)
    quan=models.Foreignkey(CartItem)