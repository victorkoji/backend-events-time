from orator import SoftDeletes
from orator.orm import belongs_to, accessor
from models.product_category import ProductCategoryModel
from models.base_model import BaseModel
import json


class ProductModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'products'
    __fillable__ = [
        'name', 'price', 'custom_form_template', 'product_category_id'
    ]
    __dates__ = ['deleted_at']
    __timestamps__ = True

    @belongs_to
    def product_category(self):
        return ProductCategoryModel
