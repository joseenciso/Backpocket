from django.test import TestCase
from .models import Product
import random

class TestViews(TestCase):
    def test_all_products_page(self):
        response = self.client.get("/allproducts/")
        self.assertEqual(response.status_code, 200)
        self.assesertTemplateUSed(response, 'products/all_products.html')

    def test_products_details_page(self):
        response = self.client.get(f'/product/details/{Product.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assesertTemplateUSed(response, 'products/product.html')