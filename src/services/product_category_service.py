from models.product_category import ProductCategoryModel
from exceptions.product_category_exception import DatabaseError


class ProductCategoryService:
    def __init__(self):
        pass

    def get(self, product_category_id=None):
        product_categories = None

        if product_category_id:
            product_categories = ProductCategoryModel.find(product_category_id)
        else:
            product_categories = ProductCategoryModel.all()

        return product_categories

    def add(self, data):
        product_category = ProductCategoryModel()

        for key, value in data.items():
            setattr(product_category, key, value)

        product_category.user_created = 1
        product_category.user_modified = 1

        try:
            product_category.save()
        except:
            raise DatabaseError('Could not save!')

        return product_category

    def update(self, data):
        product_category = ProductCategoryModel.find(data['id'])

        for key, value in data.items():
            setattr(product_category, key, value)

        try:
            product_category.save()
        except:
            raise DatabaseError('Could not update!')

        return product_category

    def delete(self, product_id):
        try:
            product_category = ProductCategoryModel.find(product_id)
            product_category.delete()
        except:
            raise DatabaseError('Could not delete!')

        return product_category
