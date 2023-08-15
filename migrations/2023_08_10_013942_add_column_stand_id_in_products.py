from orator.migrations import Migration


class AddColumnStandIdInProducts(Migration):

    def up(self):
        with self.schema.table('products') as table:
            table.integer('stand_id')
            table.foreign('stand_id').references('id').on('stands')


    def down(self):
        with self.schema.table('stands') as table:
            table.drop_foreign('products_stand_id_foreign')
            table.drop_column('stand_id')
