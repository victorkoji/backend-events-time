from orator import SoftDeletes
from models.base_model import BaseModel


class ProductCategoryModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'product_categories'
    __fillable__ = ['name']
    __dates__ = ['deleted_at']
    __timestamps__ = True
