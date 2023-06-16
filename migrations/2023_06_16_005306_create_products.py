from orator.migrations import Migration

class CreateProducts(Migration):
    def up(self):
        with self.schema.create('products') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()
            table.soft_deletes()


    def down(self):
        self.schema.drop('products')

