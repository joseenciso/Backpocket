from django.test import TestCase
from .models import Product
import random

class TestViews(TestCase):
    def test_all_products_page(self):
        response = self.client.get("/allproducts/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/allproducts.html')

    