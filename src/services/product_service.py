import json

from models.product import ProductModel
from exceptions.product_exception import DatabaseError, ProductNotFound
from config.database_config import db
from utils.logger import Logger


class ProductService:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def get(self, product_id=None):
        products = None

        if product_id:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ).find(product_id)
        else:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ).get()

        return products

    def add(self, data):
        product = ProductModel()

        for key, value in data.items():
            setattr(product, key, value)

        product.custom_form_template = json.dumps(
            data['custom_form_template']
        )

        product.user_created = 1
        product.user_modified = 1

        try:
            with db.transaction():
                product.save()
        except Exception as ex:
            self.logger.error(ex)
            raise DatabaseError('Could not save!') from ex

        return product

    def update(self, data):
        product = ProductModel.find(data['id'])

        if product is None:
            raise ProductNotFound()

        for key, value in data.items():
            setattr(product, key, value)

        product.custom_form_template = json.dumps(
            data['custom_form_template']
        )

        try:
            with db.transaction():
                product.save()
        except Exception as ex:
            self.logger.error(ex)
            raise DatabaseError('Could not update!') from ex

        return product

    def delete(self, product_id):
        product = ProductModel.find(product_id)

        if product is None:
            raise ProductNotFound()

        try:
            with db.transaction():
                product.delete()
        except Exception as ex:
            self.logger.error(ex)
            raise DatabaseError('Could not delete!') from ex

        return product
