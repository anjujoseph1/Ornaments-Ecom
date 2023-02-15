from django.db import models

# Create your models here.

class Categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True) 
    def __str__(self):
        return self.name   

class Products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(Categ,on_delete=models.CASCADE)   

   