import factory
from orator.orm import Factory
from models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
