from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('product_view/<str:pk>/',views.productdetails,name='product_view'),
]