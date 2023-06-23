import pytest

# from app import app
from src.controllers.product_controller import ProductController
from tests.factories.product_factory import ProductFactory
from unittest import TestCase
from unittest.mock import patch, MagicMock
from flask import Flask


@patch('src.controllers.product_controller.ProductService')
class TestProductController(TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_products_all(self, product_service_mock):
        # GIVEN
        ProductController(self.app)
        client = self.app.test_client()

        mock_product_service_instance = product_service_mock.return_value
        mock_product_service_instance.get_all.return_value = [
            ProductFactory(id=1, name="Product 1"),
            ProductFactory(id=2, name="Product 2"),
        ]

        # WHEN
        response = client.get('/products')

        # THEN
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [
            {'id': 1, 'name': 'Product 1'},
            {'id': 2, 'name': 'Product 2'}
        ])
        mock_product_service_instance.get_all.assert_called_once()
