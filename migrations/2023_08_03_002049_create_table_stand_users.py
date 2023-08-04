from orator.migrations import Migration


class CreateTableStandUsers(Migration):

    def up(self):
        with self.schema.create('user_event_stands') as table:
            table.integer('user_id')
            table.foreign('user_id').references('id').on('users')
            table.integer('event_id')
            table.foreign('event_id').references('id').on('events')
            table.integer('stand_id')
            table.foreign('stand_id').references('id').on('stands')
            table.boolean('is_responsible')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.integer('user_modified').unsigned().nullable()
            table.foreign('user_modified').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

            table.primary(['user_id', 'event_id', 'stand_id'])

    def down(self):
        self.schema.drop('user_event_stands')
