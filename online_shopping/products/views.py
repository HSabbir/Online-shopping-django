import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Product,Order,OrderItem
from accounts.models import Customer

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
    qs = Product.objects.search(query=query)
    categorys = getCategorys()
    context = {
        "products": qs,
        "categorys": categorys
    }
    return render(request, "product.html", context=context)


def getCartItem(request):
    try:
        order = Order.objects.filter(customer__user=request.user,completed=False).first()
        order_items = OrderItem.objects.filter(order = order)

        context = {
            "order_items": order_items
        }
        return render(request, "shoping-cart.html", context=context)
    except:
        return render(request,"shoping-cart.html",context={})

def createItem(order,productId):
    product = Product.objects.filter(id=productId).first()
    item = OrderItem.objects.create(order=order, product=product)

    return item


def updateProduct(request):
    data = json.loads(request.body)

    productId = data["productId"]
    action = data["action"]

    orders = Order.objects.filter(customer__user=request.user, completed=False)
    if orders.exists():
        order = orders.first()
        item = OrderItem.objects.filter(order=order,product__id=productId).first()

        if item is None:
            item = createItem(order,productId)

    else:
        try:
            customer = Customer.objects.filter(user=request.user).first()
        except:
            customer = Customer.objects.create(user=request.user)
            customer.save()

        order = Order.objects.create(customer=customer,completed=False,transaction_id='')
        item = createItem(order, productId)

    try:
        if action == 'add':
            item.quantity = item.quantity + 1
            item.save()
            order.save()
    except:
        return JsonResponse('not added ', safe = False)

    print(productId,action)
    return JsonResponse('updated', safe = False)

