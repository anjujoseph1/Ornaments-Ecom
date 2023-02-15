from django.shortcuts import render,redirect
from ornaments_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from.models import *
# Create your views here.

def cartprodt(request,tot=0,count=0,carti=None):
    try:
        cartl=CartList.objects.get(cart_id=c_id(requrement))
        carti=CartItems.objects.filiter(cartli=cartl)
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
        cartte=CartItems.objects.get(produ=prot,ct=cartli)
        if cartte.quantity<cartte.prot.stock:
            cartte.quantity += 1
            cartte.save()
    except CartItems.DoesNotExist:
        cartte=CartItems.objects.create(prodd=prot,quantity=1,ct=cartli)
        cartte.save()
    return redirect('cartdet')    
            
