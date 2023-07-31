from models.stand_category import StandCategoryModel
from exceptions.stand_category_exception import DatabaseError


class StandCategoryService:
    def __init__(self):
        pass

    def get(self, stand_category_id=None):
        stand_categories = None

        if stand_category_id:
            stand_categories = StandCategoryModel.find(stand_category_id)
        else:
            stand_categories = StandCategoryModel.all()

        return stand_categories

    def add(self, data):
        stand_category = StandCategoryModel()

        for key, value in data.items():
            setattr(stand_category, key, value)

        stand_category.user_created = 1
        stand_category.user_modified = 1

        try:
            stand_category.save()
        except:
            raise DatabaseError('Could not save!')

        return stand_category


    def update(self, data):
        stand_category = StandCategoryModel.find(data['id'])

        for key, value in data.items():
            setattr(stand_category, key, value)

        try:
            stand_category.save()
        except:
            raise DatabaseError('Could not update!')

        return stand_category

    def delete(self, stand_category_id):
        try:
            stand_category = StandCategoryModel.find(stand_category_id)
            stand_category.delete()
        except:
            raise DatabaseError('Could not delete!')

        return stand_category
