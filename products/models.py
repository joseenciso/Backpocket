from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    # sku = models.CharField(max_length=254, null=False)
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254)

    # String method
    def __str__(self):
        return self.name

    def get_friendly_name(self):
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
    
    def get_friendly_name(self):
        return self.friendly_name


class Articles(models.Model):
    class Meta:
        verbose_name_plural = 'Articles'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)
    sub_categories = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Gender(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, blank=False, default='SKU')
    name = models.CharField(
        max_length=250, blank=False, default='Product Name')
    categories = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # In case that category is deleted, the product will stay as NULL
    sub_categories = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)
    articles = models.ForeignKey(
        'Articles', null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey(
        'Gender', blank=False, null=True, on_delete=models.SET_NULL)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    
    brand = models.CharField(max_length=50, blank=False, default='Brand')
    base_colour = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField(blank=True)
    usage = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=False, default='Description')
    image_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
