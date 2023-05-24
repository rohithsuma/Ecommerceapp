from rest_framework import serializers
from . import models
from dataclasses import fields



#create serializers here

class SellerSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Seller
         fields = ["id","user","address"]
         
         def __init__ (self,*args,**kwargs):
             super(SellerSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
    

class SellerDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Seller
         fields = ["id","user","address"]
         def __init__ (self,*args,**kwargs):
             super(SellerDetailSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
             
             
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model =models.Product
        fields="__all__"
        def __init__ (self,*args,**kwargs):
             super(ProductSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
             
class ProductDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Product
         fields = ["id","user","address"]
         def __init__ (self,*args,**kwargs):
             super(ProductDetailSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
             
    
    
class BuyerSerializer(serializers.ModelSerializer):
    class Meta :
        model =models.Buyer
        fields="__all__"
        def __init__ (self,*args,**kwargs):
             super(BuyerSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
             
             
class BuyerDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Buyer
         fields = ["id","user","address"]
         def __init__ (self,*args,**kwargs):
             super(BuyerDetailSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
                          
             
             
             
             
             
class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model =models.Order
        fields="__all__"
        def __init__ (self,*args,**kwargs):
             super(OrderSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
    
    
class OrderDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Order
         fields = ["id","user","address"]
         def __init__ (self,*args,**kwargs):
             super(OrderDetailSerializer,self).__init__(*args,**kwargs)
             self.Meta.depth = 1
             
    
    
    