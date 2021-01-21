from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name="allproducts"),
    path('product/details/<int:pk>/', views.product, name="product"),
    path('add_new_product/', views.add_new_product, name="add_new_product"),
]
