from orator import SoftDeletes
from orator.orm import belongs_to
from models.product_category import ProductCategoryModel
from models.stand import StandModel
from models.product_file import ProductFileModel
from models.base_model import BaseModel


class ProductModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'products'
    __fillable__ = [
        'name', 'price', 'custom_form_template', 'product_category_id', 'stand_id', 'product_file_id'
    ]
    __dates__ = ['deleted_at']
    __timestamps__ = True

    @belongs_to
    def product_category(self):
        return ProductCategoryModel

    @belongs_to
    def stand(self):
        return StandModel

    @belongs_to
    def product_file(self):
        return ProductFileModel
