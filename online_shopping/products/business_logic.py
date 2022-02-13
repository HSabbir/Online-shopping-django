from django.utils import timezone

from .models import Product, ProductCategory


from datetime import datetime

def getProductData():
    products = Product.objects.all()
    categorys = ProductCategory.objects.all()

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
        'categorys': categorys,
        'recent_products': recent_products,
        'recent_products_demo': recent_products_demo
    }

    return context