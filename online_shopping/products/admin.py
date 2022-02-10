from django.contrib import admin

from .models import Product,ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'images','price','available_stock','added_time','updated_time']
    search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'added_time','updated_time']

admin.site.register(ProductCategory,ProductCategoryAdmin)
