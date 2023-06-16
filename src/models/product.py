from orator import Model, SoftDeletes

class Product(Model, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'products'
    __dates__ = ['deleted_at']
    __timestamps__ = True
