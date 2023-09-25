from django.contrib import admin

from .models import Product, Packing1, Packing2, Packing3

admin.site.register(Packing1)
admin.site.register(Packing2)
admin.site.register(Packing3)
admin.site.register(Product)
