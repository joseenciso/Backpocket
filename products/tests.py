from django.test import TestCase
from django.urls import reverse, resolve
import random

class TestDjango(TestCase):
    def test_detail_url(self):
        path = reverse('product', kwargs={'pk': random.randint(1, 40)})
        assert resolve(path).view_name == 'product'