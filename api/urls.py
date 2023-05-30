 


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("seller/",views.SellerListView.as_view()),
    path("seller/<int:pk>/",views.SellerDetailView.as_view()),
    path("seller/<int:pk>/update/",views.SellerUpdateView.as_view()),
    path("seller/<int:pk>/delete/",views.SellerDeleteView.as_view()),
    
    
    #product
    path("product/",views.ProductListView.as_view()),
    path("product/<int:pk>/",views.ProductDetailView.as_view()),
    path("product/<int:pk>/update/",views.ProductUpdateView.as_view()),
    path("product/<int:pk>/delete/",views.ProductDeleteView.as_view()),
    
    
    #order
    
    path("order/",views.OrderListView.as_view()),
    path("order/<int:pk>/",views.OrderDetailView.as_view()),
    path("order/<int:pk>/update/",views.OrderUpdateView.as_view()),
    path("order/<int:pk>/delete/",views.OrderDeleteView.as_view()),
    
    
    
]
