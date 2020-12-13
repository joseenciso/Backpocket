from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name="allproducts"),
    path('<pk>', views.product, name="product"),

]
