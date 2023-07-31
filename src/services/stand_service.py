from models.stand import StandModel
from exceptions.stand_exception import DatabaseError


class StandService:
    def __init__(self):
        pass

    def get(self, stand_id=None):
        stands = None

        if stand_id:
            stands = StandModel.find(stand_id)
        else:
            stands = StandModel.all()

        return stands

    def add(self, data):
        stand = StandModel()

        for key, value in data.items():
            setattr(stand, key, value)

        stand.user_created = 1
        stand.user_modified = 1

        try:
            stand.save()
        except:
            raise DatabaseError('Could not save!')

        return stand


    def update(self, data):
        stand = StandModel.find(data['id'])

        for key, value in data.items():
            setattr(stand, key, value)

        try:
            stand.save()
        except:
            raise DatabaseError('Could not update!')

        return stand


    def delete(self, stand_id):
        try:
            stand = StandModel.find(stand_id)
            stand.delete()
        except:
            raise DatabaseError('Could not delete!')

        return stand
