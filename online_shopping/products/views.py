from django.shortcuts import render
from django.utils import timezone

from .business_logic import getProductData, getProductById, getProductByCategory

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

