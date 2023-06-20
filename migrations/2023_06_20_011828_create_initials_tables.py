from orator.migrations import Migration


class CreateInitialsTables(Migration):

    def up(self):
        with self.schema.create('user_groups') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('users') as table:
            table.increments('id')
            table.string('first_name')
            table.string('last_name')
            table.date('birth_date')
            table.string('email')
            table.string('cellphone')
            table.string('password')
            table.integer('user_group').unsigned()
            table.foreign('user_group').references('id').on('user_groups')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('events') as table:
            table.increments('id')
            table.string('name')
            table.datetime('programmed_date_initial')
            table.datetime('programmed_date_final')
            table.string('address')
            table.boolean('is_public')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('stand_categories') as table:
            table.increments('id')
            table.string('name')
            table.integer('event_id')
            table.foreign('event_id').references('id').on('events')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('stands') as table:
            table.increments('id')
            table.boolean('name')
            table.integer('responsible')
            table.foreign('responsible').references('id').on('users')
            table.integer('stand_category_id')
            table.foreign('stand_category_id').references('id').on('stand_categories')
            table.integer('event_id')
            table.foreign('event_id').references('id').on('events')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('product_categories') as table:
            table.increments('id')
            table.string('name')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('products') as table:
            table.increments('id')
            table.string('name')
            table.integer('quantity')
            table.float('price')
            table.integer('product_category_id').unsigned()
            table.foreign('product_category_id').references('id').on('product_categories')
            table.integer('user_created').unsigned()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()
            
        with self.schema.create('menu') as table:
            table.increments('id')
            table.integer('stand_id')
            table.foreign('stand_id').references('id').on('stands')
            table.integer('product_id')
            table.foreign('product_id').references('id').on('products')
            table.timestamps()
            table.soft_deletes()
        pass

    def down(self):
        self.schema.drop('products')
        pass

from orator.migrations import Migration