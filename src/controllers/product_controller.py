from flask import Blueprint, jsonify, request
from services.product_service import ProductService
from models.product import Product
import json


class ProductController:
    def __init__(self, app):
        self.product_routes = Blueprint('product_routes', __name__)
        self.product_service = ProductService()

        self.register_routes()
        app.register_blueprint(self.product_routes)

    def register_routes(self):
        self.product_routes.route(
            '/products', methods=['GET'])(self.get_products)
        self.product_routes.route(
            '/products/<int:product_id>', methods=['GET'])(self.get_product)
        self.product_routes.route(
            '/products', methods=['POST'])(self.add_product)
        self.product_routes.route(
            '/products/<int:product_id>', methods=['PUT'])(self.update_product)
        self.product_routes.route(
            '/products/<int:product_id>', methods=['DELETE'])(self.delete_product)

    def get_products(self):
        products = self.product_service.get_all()
        product_data = [{'id': product.id, 'name': product.name}
                        for product in products]
        return jsonify(product_data)

    def get_product(self, product_id):
        product = self.product_service.get_product(product_id)
        if product:
            product_data = {'id': product.id, 'name': product.name}
            return jsonify(product_data)
        else:
            return jsonify({'error': 'Product not found'}), 404

    def add_product(self):
        data = request.get_json()
        product = Product()
        product.name = data['name']
        self.product_service.add_product(product)
        return jsonify({'message': 'Product added successfully'}), 201

    def update_product(self, product_id):
        data = request.get_json()
        if self.product_service.update_product(product_id, data['name']):
            return jsonify({'message': 'Product updated successfully'})
        else:
            return jsonify({'error': 'Product not found'}), 404

    def delete_product(self, product_id):
        if self.product_service.delete_product(product_id):
            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'error': 'Product not found'}), 404
