from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    #print(products[0].image)
    return render(request, 'index.html',{'products':products})
