from models.product import Product
from exceptions.product_exception import DatabaseError


class ProductService:
    def __init__(self):
        pass

    def get_all(self):
        return Product.all()

    def get_product(self, id):
        return Product.find(id)

    def add_product(self, data):
        try:
            product = Product()
            product.name = data.name
            product.save()
        except:
            raise DatabaseError('Não foi possível salvar o produto')

        return product

    def update_product(self, data):
        try:
            product = Product.find(data.id)
            product.name = data.name
            product.save()
        except:
            raise DatabaseError('Não foi possível atualizar o produto')

        return product

    def delete_product(self, product_id):
        try:
            product = Product.find(product_id)
            product.delete()
        except:
            raise DatabaseError('Não foi possível remover o produto')

        return product
