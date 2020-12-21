from django.contrib import admin
from .models import Product, Category, Sub_Category, Articles


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'gender',
        'categories',
        'sub_categories',
        'articles',
        'usage',
        'price',
        'image',
        'image_url',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, Sub_CategoryAdmin)
admin.site.register(Articles, ArticleAdmin)
