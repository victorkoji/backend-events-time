from orator.migrations import Migration


class CreateTableProductFiles(Migration):

    def up(self):
        with self.schema.create('product_files') as table:
            table.increments('id')
            table.string('filename')
            table.string('filename_original')
            table.string('media_type', 100)
            table.string('filepath')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned().nullable()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.table('products') as table:
            table.integer('product_file_id').unsigned().nullable()
            table.foreign('product_file_id').references('id').on('product_files')

    def down(self):
        self.schema.drop('product_files')

        with self.schema.table('products') as table:
            table.drop_foreign('products_product_file_id_foreign')
            table.drop_column('product_file_id')
