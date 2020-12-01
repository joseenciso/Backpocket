from django.db import models

# Create your models here.


class Category(models.Model):
    # sku = models.CharField(max_length=254, null=False)
    category_name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

    # String method
    def __str__(self):
        return self.category_name

    def get_product_display_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # In case that category is deleted, the product will stay as NULL
    sku = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    sub_category = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    article_type = models.CharField(max_length=150, null=True, blank=True)
    base_colour = models.CharField(max_length=50, null=True, blank=True)
    season = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    usage = models.CharField(max_length=50, null=True, blank=True)
    product_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
