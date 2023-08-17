import json

from models.product import ProductModel
from services.product_category_service import ProductCategoryService
from services.product_file_service import ProductFileService
from exceptions.product_exception import ProductNotFound
from exceptions.general_exception import DatabaseError
from config.database_config import db
from utils.logger import Logger


class ProductService:
    def __init__(self):
        self.product_category_service = ProductCategoryService()
        self.product_file_service = ProductFileService()
        self.logger = Logger(self.__class__.__name__)

    def get(self, product_id=None):
        products = None

        if product_id:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ) \
            .with_('product_category', 'product_file', 'stand') \
            .find(product_id)
        else:
            products = ProductModel.select(
                '*', db.raw('custom_form_template::text')
            ) \
            .with_('product_category', 'product_file', 'stand') \
            .get()

        return products

    def get_menu_by_event_id(self, event_id):
        return self.product_category_service.get_menu_by_event_id(event_id)

    def add(self, data, file, user_id):
        product = ProductModel()

        for key, value in data.items():
            setattr(product, key, value)

        product.custom_form_template = json.dumps(
            data['custom_form_template']
        )

        product.user_created = user_id
        product.user_modified = user_id

        try:
            with db.transaction():
                product_file = self.product_file_service.save_file(file, user_id)
                product.product_file_id = product_file.id
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
