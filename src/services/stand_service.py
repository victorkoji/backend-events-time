from models.stand import StandModel


class StandService:
    def __init__(self):
        pass

    def get(self, id=None):
        stands = None

        if id:
            stands = StandModel.find(id)
        else:
            stands = StandModel.all()

        return stands

    def add(self, data):
        try:
            stand = StandModel()

            for key, value in data.items():
                setattr(stand, key, value)

            stand.user_created = 1
            stand.user_modified = 1

            stand.save()

            return stand
        except Exception as ex:
            raise Exception('Could not save!')

    def update(self, data):
        try:
            stand = StandModel.find(data['id'])

            for key, value in data.items():
                setattr(stand, key, value)

            stand.save()

            return stand
        except:
            raise Exception('Could not update!')

    def delete(self, stand_id):
        try:
            stand = StandModel.find(stand_id)
            stand.delete()
        except:
            raise Exception('Could not delete!')

        return stand
