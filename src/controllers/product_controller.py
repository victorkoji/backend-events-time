from flask import jsonify, request, Blueprint
from repositories.product_repository import ProductRepository
from models.product import Product

# Criar a blueprint
product_routes = Blueprint('product_routes', __name__)

product_repository = ProductRepository()

@product_routes.route('/products', methods=['GET'])
def get_items():
    items = product_repository.get_all_items()
    item_data = [{'id': item.id} for item in items]
    return jsonify(item_data)

@product_routes.route('/products/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = product_repository.get_item(item_id)
    if item:
        item_data = {'id': item.id, 'name': item.name}
        return jsonify(item_data)
    else:
        return jsonify({'error': 'Product not found'}), 404

@product_routes.route('/products', methods=['POST'])
def add_item():
    data = request.get_json()
    item = Product(data['id'], data['name'])
    product_repository.add_item(item)
    return jsonify({'message': 'Product added successfully'}), 201

@product_routes.route('/products/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if product_repository.update_item(item_id, data['name']):
        return jsonify({'message': 'Product updated successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404

@product_routes.route('/products/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if product_repository.delete_item(item_id):
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404