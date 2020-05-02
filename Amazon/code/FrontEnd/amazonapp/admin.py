from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AUser)
admin.site.register(Order)
admin.site.register(Warehouse)
admin.site.register(PurchasedProduct)
admin.site.register(Cart)