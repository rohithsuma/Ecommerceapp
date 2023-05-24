from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics,permissions



class SellerList(generics.ListCreateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class =serializers.SellerSerializer
   # parser_classes = [permissions.IsAuthenticated]
    
    
class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Seller.objects.all()
    serializer_class =serializers.SellerDetailSerializer
    #parser_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class =serializers.ProductSerializer
   # parser_classes = [permissions.IsAuthenticated]
    
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class =serializers.ProductDetailSerializer
    #parser_classes = [permissions.IsAuthenticated]



class BuyerList(generics.ListCreateAPIView):
    queryset = models.Buyer.objects.all()
    serializer_class =serializers.BuyerSerializer
   # parser_classes = [permissions.IsAuthenticated]
    
    
class BuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Buyer.objects.all()
    serializer_class =serializers.BuyerDetailSerializer
    #parser_classes = [permissions.IsAuthenticated]
    
    
    
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class =serializers.OrderSerializer
   # parser_classes = [permissions.IsAuthenticated]
    
    
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class =serializers.OrderDetailSerializer
    #parser_classes = [permissions.IsAuthenticated]




