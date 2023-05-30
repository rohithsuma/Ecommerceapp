 


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Seller
    path("seller/",views.SellerList.as_view()),
    path("sellerDetail/<int:pk>/",views.SellerList.as_view()),
    #product
    path("product/",views.ProductList.as_view()),
    path("sellerDetail/<int:pk>/",views.ProductList.as_view()),
    
    #Buyers
    path("buyer/",views.BuyerList.as_view()),
    path("buyerDetail/<int:pk>/",views.BuyerList.as_view()),
    
    #order
    
    path("order/",views.OrderList.as_view()),
    path("orderDetail/<int:pk>/",views.OrderList.as_view()),
    
    
    
]

