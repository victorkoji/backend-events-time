from models.product import ProductModel
from exceptions.custom_exception import DatabaseError
import json
from config.database_config import db


class ProductService:
    def __init__(self):
        pass

    def get(self, id=None):
        products = None

        if id:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ).find(id)
        else:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ).get()

        return products

    def add(self, data):
        try:
            product = ProductModel()

            for key, value in data.items():
                setattr(product, key, value)

            product.custom_form_template = json.dumps(
                data['custom_form_template']
            )

            product.user_created = 1
            product.user_modified = 1

            product.save()

            return product
        except Exception as ex:
            print(ex)
            raise DatabaseError('Could not save!')

    def update(self, data):
        try:
            product = ProductModel.find(data['id'])

            for key, value in data.items():
                setattr(product, key, value)

            product.custom_form_template = json.dumps(
                data['custom_form_template']
            )

            product.save()

            return product
        except:
            raise DatabaseError('Could not update!')

    def delete(self, product_id):
        try:
            product = ProductModel.find(product_id)
            product.delete()
        except:
            raise DatabaseError('Could not delete!')

        return product
