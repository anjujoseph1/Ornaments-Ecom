from django.urls import path
from.import views

urlpatterns=[
    path('cartt/',views.cartprodt,name='cartdet'),+
    path('add/<int:product_id>/',views.addcart,name='addcart'),
    path('dicrement/<int:prodt_id>/',views.dicrement,name='dicrement'),
    path('delete/<int:pt_id>/',views.delete,name='delete'),
]