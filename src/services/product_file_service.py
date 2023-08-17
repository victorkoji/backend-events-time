import os
import uuid

from models.product_file import ProductFileModel
from services.product_category_service import ProductCategoryService
from exceptions.product_file_exception import ProductFileNotFound, UploadFailedError
from exceptions.general_exception import DatabaseError
from config.database_config import db
from utils.logger import Logger


class ProductFileService:
    def __init__(self):
        self.product_category_service = ProductCategoryService()
        self.logger = Logger(self.__class__.__name__)

    def save_file(self, file, user_id):
        product_file = ProductFileModel()

        filename, filepath = self._upload_file(file).values()
        product_file.filename = filename
        product_file.filepath = filepath
        product_file.filename_original = file.filename.replace(" ", "-")
        product_file.media_type = file.content_type
        product_file.user_created = user_id
        product_file.user_modified = user_id

        try:
            product_file.save()
        except Exception as ex:
            self.logger.error(ex)
            raise DatabaseError('Could not save!') from ex

        return product_file

    def delete(self, product_id):
        product_file = ProductFileModel.find(product_id)

        if product_file is None:
            raise ProductFileNotFound()

        try:
            with db.transaction():
                product_file.delete()
        except Exception as ex:
            self.logger.error(ex)
            raise DatabaseError('Could not delete!') from ex

        return product_file

    def _upload_file(self, file):
        try:
            contents = file.file.read()
            filename = self._generate_uuid_from_filename(file.filename)
            filepath = f"/public/images/{filename}"

            with open(f"{os.getcwd()}{filepath}", 'wb') as f:
                f.write(contents)
        except Exception as ex:
            raise UploadFailedError() from ex
        finally:
            file.file.close()

        return {"filename": filename, "filepath": filepath}

    def _generate_uuid_from_filename(self, filename):
        image_extension = filename.split(".")[-1]
        unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        uuid_filename = f"{unique_id}.{image_extension}"
        return uuid_filename
