from django.shortcuts import render
from django.utils import timezone

from .business_logic import getProductData
def index(request):
    context = getProductData()

    return render(request, 'index.html', context)


def product(request):
    context = getProductData()

    return render(request, 'product.html', context)
