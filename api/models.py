from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.

class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null= True)
    email = models.EmailField(default='example@example.com')
    password=models.CharField(max_length=10,default='password')
    
    def __str__(self):
        return self.user.username



class Product(models.Model):
    title = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)
    detail = models.TextField(null=True)
    price = models.FloatField()
    registered_at = models.DateTimeField(default=datetime.now(), blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    

    
class Order(models.Model):
    buyer = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    orderTime = models.DateTimeField(auto_now_add=True)