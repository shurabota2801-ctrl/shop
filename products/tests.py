from django.test import TestCase
from .models import Product, Category
from decimal import Decimal


class TestProductModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='категория1',
            slug='kategorya-1'
        )

        self.product = Product.objects.create(
            category=self.category,
            name='товар1',
            slug='tovar-1',
            price=300,
        )

    def test_product_price(self):
        self.assertEqual(self.product.price, Decimal('300'))

    def test_count_object(self):
        product = Product.objects.count()
        self.assertEqual(product, 1)