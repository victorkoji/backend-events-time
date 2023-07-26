from models.product_category import ProductCategoryModel


class ProductCategoryService:
    def __init__(self):
        pass

    def get(self, id=None):
        product_categories = None

        if id:
            product_categories = ProductCategoryModel.find(id)
        else:
            product_categories = ProductCategoryModel.all()

        return product_categories

    def add(self, data):
        try:
            product_category = ProductCategoryModel()

            for key, value in data.items():
                setattr(product_category, key, value)

            product_category.user_created = 1
            product_category.user_modified = 1

            product_category.save()

            return product_category
        except:
            raise Exception('Could not save!')

    def update(self, data):
        try:
            product_category = ProductCategoryModel.find(data['id'])

            for key, value in data.items():
                setattr(product_category, key, value)

            product_category.save()

            return product_category
        except:
            raise Exception('Could not update!')

    def delete(self, product_id):
        try:
            product_category = ProductCategoryModel.find(product_id)
            product_category.delete()
        except:
            raise Exception('Could not delete!')

        return product_category
