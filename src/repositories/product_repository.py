from models.product import Product

class ProductRepository:
    def get_all_items(self):
        return Product.all()

    def get_item(self, item_id):
        return Product.find(item_id)

    def add_item(self, item):
        product = Product()

        try:
            product.save()
        except:
            raise Exception("Ocorreu um erro ao salvar o produto")

        return product

    def update_item(self, item_id, name):
        product = Product.find(item_id)
        product.name = name

        try:
            product.save()
        except:
            raise Exception("Ocorreu um erro ao salvar o produto")

        return product

    def delete_item(self, item_id):
        product = Product.find(item_id)
        return product.delete()
