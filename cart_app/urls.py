from django.urls import path
from.import views

urlpatterns=[
    path('cartt/',views.cartprodt,name='cartdet'),
    path('add/<int:product_id>/',views.addcart,name='addcart'),
]