from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'price','available_stock','added_time','updated_time']
    search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)
