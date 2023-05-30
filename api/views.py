from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics,permissions



class SellerListView(generics.ListCreateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class =serializers.SellerSerializer
    
   
class SellerDetailView(generics.RetrieveAPIView):
    queryset = models.Seller.objects.all()
    serializer_class =serializers.SellerSerializer
    lookup_field = "pk"
    
class SellerUpdateView(generics.UpdateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    lookup_field  = 'pk'

class SellerDeleteView (generics.DestroyAPIView):
    queryset = models.Seller.objects.all()  
    serializer_class = serializers.SellerSerializer
    lookup_field = 'pk'
    
    
   

    
    


class ProductListView (generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class =serializers.ProductSerializer
   # Provide both list and create operations for the model
   
   
class ProductDetailView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class =serializers.ProductSerializer
    lookup_field = "pk"
    
class ProductUpdateView(generics.UpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field  = 'pk'

class ProductDeleteView (generics.DestroyAPIView):
    queryset = models.Product.objects.all()  
    serializer_class = serializers.ProductSerializer
    lookup_field = 'pk'
    
    





    
    
    
class OrderListView(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class =serializers.OrderSerializer
   # Provide both list and create operations for the model
 
class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class =serializers.OrderSerializer
    lookup_field = "pk"
    
class OrderUpdateView(generics.UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field  = 'pk'

class OrderDeleteView (generics.DestroyAPIView):
    queryset = models.Order.objects.all()  
    serializer_class = serializers.OrderSerializer
    lookup_field = 'pk'
    



