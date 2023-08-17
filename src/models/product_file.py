from orator import SoftDeletes
from models.base_model import BaseModel


class ProductFileModel(BaseModel, SoftDeletes):
    __schema__ = 'public'
    __table__ = 'product_files'
    __fillable__ = [
        'filename', 'filename_original', 'media_type', 'filepath'
    ]
    __dates__ = ['deleted_at']
    __timestamps__ = True
