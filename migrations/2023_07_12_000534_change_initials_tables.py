from orator.migrations import Migration


class ChangeInitialsTables(Migration):

    def up(self):
        with self.schema.table('users') as table:
            table.string('token_fcm').nullable()

        with self.schema.table('stands') as table:
            table.string('name').change()
            table.boolean('is_cashier').default(False)
            table.drop_foreign('stands_responsible_foreign')
            table.drop_column('responsible')

        with self.schema.table('product_categories') as table:
            table.integer('event_id')
            table.foreign('event_id').references('id').on('events')

        with self.schema.table('events') as table:
            table.date('programmed_date_initial').nullable().change()
            table.date('programmed_date_final').nullable().change()

        sql = '''
            ALTER TABLE products
            ADD COLUMN custom_form_template jsonb;
        '''

        self.db.statement(sql)

    def down(self):
        with self.schema.table('users') as table:
            table.drop_column('token_fcm')

        with self.schema.table('stands') as table:
            table.drop_column('is_cashier')
            table.integer('responsible')
            table.foreign('responsible').references('id').on('users')

        with self.schema.table('product_categories') as table:
            table.drop_foreign('product_categories_event_id_foreign')
            table.drop_column('event_id')

        with self.schema.table('events') as table:
            table.datetime('programmed_date_initial').nullable().change()
            table.datetime('programmed_date_final').nullable().change()

        sql = '''
            ALTER TABLE products
            DROP COLUMN custom_form_template;
        '''

        self.db.statement(sql)
