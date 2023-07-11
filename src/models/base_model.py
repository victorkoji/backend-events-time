from orator import Model


class BaseModel(Model):
    @classmethod
    def find_by_column(cls, **kwargs):
        query = cls
        for column, value in kwargs.items():
            query = query.where(column, value)
        return query.first()
