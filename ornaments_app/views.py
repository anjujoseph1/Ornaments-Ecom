from django.shortcuts import render
from.models import *
# Create your views here.

def home(request):
    product=Products.objects.all()
    return render(request,'home.html',{'pro':product})

def productdetails(request,pk):
    prodet=Products.objects.get(id=pk)
    return render (request,'product.html',{'pr':prodet})    