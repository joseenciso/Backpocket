from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    # sku = models.CharField(max_length=254, null=False)
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

    # String method
    def __str__(self):
        return self.name

    def get_product_display_name(self):
        return self.friendly_name


class Sub_Category(models.Model):
    class Meta:
        verbose_name_plural = 'Sub_categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)
    categories = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Articles(models.Model):

    class Meta:
        verbose_name_plural = 'Articles'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)
    sub_categories = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # In case that category is deleted, the product will stay as NULL
    sub_categories = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=False, default='SKU')
    gender = models.CharField(
        max_length=25, blank=False, default='Men, Women, Unisex')
    brand = models.CharField(max_length=50, blank=False, default='Band')
    articles = models.ForeignKey(
        'Articles', null=True, blank=True, on_delete=models.SET_NULL)
    base_colour = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True)
    usage = models.CharField(max_length=50, blank=True)
    name = models.CharField(
        max_length=250, blank=False, default='Product Name')
    description = models.TextField(blank=False, default='Description')
    image_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
