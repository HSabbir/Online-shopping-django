from django.shortcuts import render
from .models import Product, ProductCategory

def index(request):
    products = Product.objects.all()
    categorys = ProductCategory.objects.all()
    context = {
        'products': products,
        'categorys' : categorys
    }
    return render(request, 'index.html',context)
