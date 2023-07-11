from models.product import ProductModel
from exceptions.custom_exception import DatabaseError


class ProductService:
    def __init__(self):
        pass

    def get(self, id=None):
        products = None

        if id:
            products = ProductModel.find(id)
        else:
            products = ProductModel.all()

        return products

    def add(self, data):
        try:
            product = ProductModel()

            for key, value in data.items():
                setattr(product, key, value)

            product.user_created = 1
            product.user_modified = 1

            return product.save()
        except:
            raise DatabaseError('Could not save!')

    def update(self, data):
        try:
            product = ProductModel.find(data['id'])

            for key, value in data.items():
                setattr(product, key, value)

            return product.save()
        except:
            raise DatabaseError('Could not update!')

    def delete(self, product_id):
        try:
            product = ProductModel.find(product_id)
            product.delete()
        except:
            raise DatabaseError('Could not delete!')

        return product
