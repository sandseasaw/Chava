from django.contrib import admin
from myapp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','desc0','type0','size0','price']


admin.site.register(Product, ProductAdmin)