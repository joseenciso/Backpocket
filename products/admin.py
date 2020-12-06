from django.contrib import admin
from .models import Product, Category, Sub_Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product_name',
        'gender',
        'categories',
        'sub_categories',
        'article_type',
        'usage',
        'price',
        'image',
        'image_url',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'category_name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category)
