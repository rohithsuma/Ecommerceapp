from rest_framework import serializers
from . import models
from dataclasses import fields



#create serializers here

class SellerSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Seller
         fields = "__all__"
         
          
    
 
             
class ProductSerializer(serializers.ModelSerializer):
    is_enabled = serializers.BooleanField(default=True, write_only=True)
    class Meta :
        model =models.Product
        fields="__all__"
        
        
             
class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model =models.Order
        fields="__all__"
         
    
    
 
    
    