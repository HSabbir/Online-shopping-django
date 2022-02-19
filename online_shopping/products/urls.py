from django.urls import path

from . import views

urlpatterns = [
    path('', views.product , name = "products"),
    path('<str:category>/', views.filter_products, name="filter_products"),
    path('product_details/<str:slug>/', views.product_details , name = "product_details"),
]