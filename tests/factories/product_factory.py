import factory
from orator.orm import Factory
from models.product import Product
from tests.config.database_config import database


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
