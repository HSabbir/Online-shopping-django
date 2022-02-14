from django.urls import path

from . import views

urlpatterns = [
    path('', views.product , name = "products"),
    path('product_details/<int:id>/', views.product_details , name = "product_details")
]