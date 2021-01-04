from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name="shopping_bag"),
    path('add/<product_pk>/', views.view_add_to_bag, name="add_to_bag"),
    path('edit/<product_pk>/', views.view_edit_bag, name="edit_bag"),
    path('remove/<product_pk>/', views.view_remove_from_bag, name="remove_bag")
]
