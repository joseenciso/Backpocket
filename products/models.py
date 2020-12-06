from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    # sku = models.CharField(max_length=254, null=False)
    category_name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

    # String method
    def __str__(self):
        return self.category_name

    def get_product_display_name(self):
        return self.friendly_name


class Sub_Category(models.Model):
    sub_category_name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # In case that category is deleted, the product will stay as NULL
    sku = models.CharField(max_length=254, blank=False, default='SKU')
    gender = models.CharField(
        max_length=25, blank=False, default='Men, Women, Unisex')
    categories = models.CharField(
        max_length=50, blank=False, default='Category')
    sub_categories = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=False, default='Band')
    article_type = models.CharField(
        max_length=150, blank=False, default='Article Type')
    base_colour = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    usage = models.CharField(max_length=50, blank=True)
    product_name = models.CharField(
        max_length=250, blank=False, default='Product Name')
    description = models.TextField(blank=False, default='Description')
    image_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.product_name
