from models.product_category import ProductCategoryModel
from models.product import ProductModel
from exceptions.general_exception import DatabaseError


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


    def get_menu_by_event_id(self, event_id):
        categories = ProductCategoryModel \
            .with_({
                'products': lambda q: q
                    .order_by(f'{ProductModel.__table__}.name')
                    .with_('stand', 'product_file')
            }) \
            .where('event_id', event_id) \
            .order_by(f'{ProductCategoryModel.__table__}.name') \
            .get()

        return categories.serialize()

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
