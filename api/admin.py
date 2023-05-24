from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Seller)
admin.site.register(models.Product)
admin.site.register(models.Buyer)
admin.site.register(models.Order)