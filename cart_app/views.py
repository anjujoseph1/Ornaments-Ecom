from django.shortcuts import render,redirect,get_object_or_404
from ornaments_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from.models import *
# Create your views here.

def cartprodt(request,tot=0,count=0,carti=None):
    try:
        cartl=CartList.objects.get(cart_id=c_id(request))
        carti=CartItems.objects.filter(cartli=cartl)
        for i in carti:
            tot += (i.prot.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
            pass    
    return render(request,'cart.html',{'cartitem':carti,'total':tot,'count':count})

def c_id(request):
    cartd=request.session.session_key
    if not cartd:
        cartd=request.session.create()
    return cartd    

def addcart(request,product_id):
    prodall=Products.objects.get(id=product_id)
    try:
        car=CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        car=CartList.objects.create(cart_id=c_id(request))
        car.save()
    try:
        cartte=CartItems.objects.get(prot=prodall,cartli=car)
        if cartte.quantity<cartte.prot.stock:
            cartte.quantity += 1
            cartte.save()
    except CartItems.DoesNotExist:
        cartte=CartItems.objects.create(prot=prodall,quantity=1,cartli=car)
        cartte.save()
    return redirect('cartdet')    
            
def dicrement(request,prodt_id):
    cart=CartList.objects.get(cartd=c_id(request))
    product=get_object_or_404(Products,id=prodt_id)
    cartem=CartItems.objects.get(prot=product,cartli=cart)
    if cartem.quantity >1:
        cartem.quantity -=1
        cartem.save()
    else:
        cartem.delete()
    return redirect('cartdet')        

def delete(request,pt_id):
    cat=CartList.objects.get(cartd=c_id(request))
    pt=get_object_or_404(Products,id=pt_id)
    cartm=CartItems.objects.get(prot=pt,cartli=cat)
    cartm.delete()
    return redirect('cartdet')
