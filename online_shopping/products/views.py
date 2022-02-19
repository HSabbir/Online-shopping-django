from django.shortcuts import render
from django.utils import timezone
from .models import Product

from .business_logic import getProductData, getProductById, getProductByCategory,getCategorys

def homeView(request):
    context = getProductData()

    return render(request, 'index.html', context)

def product(request):
    context = getProductData()

    return render(request, 'product.html', context)

def product_details(request, slug):
    context = getProductById(slug)

    return render(request, 'product_details.html', context)

def filter_products(request, category):
    context = getProductByCategory(category)
    return render(request, 'product.html',context)

def product_search(request):
    query = request.GET.get('q')
    print(query)
    qs = Product.objects.search(query=query)
    print(qs)
    categorys = getCategorys()
    context = {
        "products": qs,
        "categorys": categorys
    }
    return render(request, "product.html", context=context)

