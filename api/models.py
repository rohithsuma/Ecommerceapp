from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null= True)
    
    def __str__(self):
        return self.user.username



class Product(models.Model):
    title = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)
    detail = models.TextField(null=True)
    price = models.FloatField()
    registered_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
class Buyer (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)
    mobile = models.PositiveBigIntegerField()
    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    orderTime = models.DateTimeField(auto_now_add=True)