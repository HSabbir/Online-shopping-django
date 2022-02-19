from django.utils import timezone

from .models import Product, ProductCategory


from datetime import datetime

def getProductData():
    products = Product.objects.all()

    today = timezone.now().date()
    last_day = today - timezone.timedelta(days=7)

    today = datetime.strftime(today, "%Y-%m-%d")
    last_day = datetime.strftime(last_day, "%Y-%m-%d")

    recent_products = Product.objects.filter(added_time__range=[last_day, today]).order_by("-added_time")

    recent_products_demo = list(recent_products)
    recent_products_demo = [recent_products_demo[0:3],recent_products_demo[3:6]]

    print(recent_products_demo)
    context = {
        'products': products,
        'categorys': getCategorys(),
        'recent_products_demo': recent_products_demo
    }

    return context


def getCategorys():
    return ProductCategory.objects.all()

def getProductById(slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category = product.category).exclude(slug=slug)

    context = {
        'product': product,
        'categorys': getCategorys(),
        'related_products': related_products,
    }

    return context

def getProductByCategory(category):
    products = Product.objects.filter(category__slug = category)

    context = {
        'products' : products,
        'categorys': getCategorys(),
    }
    return context