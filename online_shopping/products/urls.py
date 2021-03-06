from django.urls import path

from . import views

urlpatterns = [
    path('', views.product , name = "products"),
    path('cart_page/', views.getCartItem, name="cart_page"),
    path('update-cart/', views.updateProduct, name='update-cart'),
    path('search_result/' , views.product_search, name="product_search"),
    path('<str:category>/', views.filter_products, name="filter_products"),
    path('product_details/<str:slug>/', views.product_details , name = "product_details")
]