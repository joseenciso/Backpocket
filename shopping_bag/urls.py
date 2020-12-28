from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name="shopping_bag"),
    path('add/<product_id>', views.view_add_to_bag, name="add_to_bag")
]
