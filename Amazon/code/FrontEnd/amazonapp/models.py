from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class AUser(AbstractUser):
    ups_name = models.CharField(max_length = 256, verbose_name = "ups username", default = "")
    location_x = models.PositiveIntegerField(verbose_name = "location x", default = 0, null = False)
    location_y = models.PositiveIntegerField(verbose_name = "location y", default = 0, null = False)

class Order(models.Model):
    owner = models.ForeignKey(AUser, on_delete = models.CASCADE, related_name = "order2user", blank = False, null = False)
    shipid = models.AutoField(verbose_name="order id", default=0, null = False, primary_key = True)
    # status = models.CharField(max_length = 256, verbose_name = "order status", choices=[("o", "ordered"), ("s", "shipped"), ("d", "delivered")])
    status = models.CharField(max_length = 256, verbose_name = "order status")
    order_description = models.CharField(max_length = 256, verbose_name = "order description", default = "")
    truckid = models.IntegerField(null = True)
    x = models.IntegerField(blank = True, null = True)
    y = models.IntegerField(blank = True, null = True)
    ups_name = models.CharField(max_length = 256, verbose_name = "ups useraccount")

class Warehouse(models.Model):
    product_id = models.AutoField(blank = False, null = False, default=0, primary_key=True)
    product_name = models.CharField(max_length = 256, verbose_name = "product name", default = "")
    total_number = models.PositiveIntegerField(default = 0, blank = False, null = False)

class PurchasedProduct(models.Model):
    shipid = models.ForeignKey(Order, on_delete = models.PROTECT, blank = True, null = True)
    product_id = models.ForeignKey(Warehouse, on_delete = models.CASCADE)
    count = models.PositiveIntegerField(verbose_name = "number", default = 0, null = False)

class Cart(models.Model):
    userid = models.ForeignKey(AUser, on_delete = models.CASCADE, related_name = "card2user", blank = False, null = False)
    product_name = models.CharField(max_length = 256, verbose_name = "product name", default = "", blank = False, null = False, primary_key = True)
    count = models.PositiveIntegerField(verbose_name = "number", default = 0, null = False)

    

