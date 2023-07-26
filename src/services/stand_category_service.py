from models.stand_category import StandCategoryModel


class StandCategoryService:
    def __init__(self):
        pass

    def get(self, id=None):
        stand_categories = None

        if id:
            stand_categories = StandCategoryModel.find(id)
        else:
            stand_categories = StandCategoryModel.all()

        return stand_categories

    def add(self, data):
        try:
            stand_category = StandCategoryModel()

            for key, value in data.items():
                setattr(stand_category, key, value)

            stand_category.user_created = 1
            stand_category.user_modified = 1

            stand_category.save()

            return stand_category
        except:
            raise Exception('Could not save!')

    def update(self, data):
        try:
            stand_category = StandCategoryModel.find(data['id'])

            for key, value in data.items():
                setattr(stand_category, key, value)

            stand_category.save()

            return stand_category
        except:
            raise Exception('Could not update!')

    def delete(self, stand_category_id):
        try:
            stand_category = StandCategoryModel.find(stand_category_id)
            stand_category.delete()
        except:
            raise Exception('Could not delete!')

        return stand_category
