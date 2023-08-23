from orator.migrations import Migration


class CreateTableBuyoutFlow(Migration):

    def up(self):
        with self.schema.create('status_charges') as table:
            table.increments('id')
            table.string('name')

        sql = '''
            INSERT INTO status_charges (id, name) VALUES
                (1, 'Pendente'),
                (2, 'Confirmado'),
                (3, 'Estornado'),
                (4, 'Cancelado');
        '''
        self.db.statement(sql)

        with self.schema.create('payment_methods') as table:
            table.increments('id')
            table.string('name', 50)

        sql = '''
            INSERT INTO payment_methods (id, name) VALUES
                (1, 'Pix'),
                (2, 'Cartão de crédito'),
                (3, 'Dinheiro');
        '''
        self.db.statement(sql)

        with self.schema.create('status_vouchers') as table:
            table.increments('id')
            table.string('name', 50)

        sql = '''
            INSERT INTO status_vouchers (id, name) VALUES
                (1, 'Aguardando'),
                (2, 'Solicitado'),
                (3, 'Utilizado'),
                (4, 'Estornado'),
                (5, 'Cancelado');
        '''
        self.db.statement(sql)

        with self.schema.create('status_stand_orders') as table:
            table.increments('id')
            table.string('name', 50)

        sql = '''
            INSERT INTO status_stand_orders (id, name) VALUES
                (1, 'Aguardando'),
                (2, 'Em andamento'),
                (3, 'Pronto para retirada'),
                (4, 'Concluido');
        '''
        self.db.statement(sql)

        with self.schema.create('stand_orders') as table:
            table.increments('id')
            table.float('total_amount')
            table.integer('num_order')
            table.integer('stand_id').unsigned().nullable()
            table.foreign('stand_id').references('id').on('stands')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('stand_order_vouchers') as table:
            table.increments('id')
            table.integer('stand_order_id').unsigned().nullable()
            table.foreign('stand_order_id').references('id').on('stand_orders')
            table.timestamps()
            table.soft_deletes()

        sql = '''
            ALTER TABLE stand_order_vouchers
            ADD COLUMN custom_response jsonb;
        '''

        self.db.statement(sql)

        with self.schema.create('buyouts') as table:
            table.increments('id')
            table.float('total_amount')
            table.boolean('approved')
            table.integer('event_id').unsigned().nullable()
            table.foreign('event_id').references('id').on('events')

            table.integer('user_owner').unsigned().nullable()
            table.foreign('user_owner').references('id').on('users')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('charges') as table:
            table.increments('id')
            table.integer('buyout_id').unsigned().nullable()
            table.foreign('buyout_id').references('id').on('buyouts')
            table.integer('payment_method_id').unsigned().nullable()
            table.foreign('payment_method_id').references('id').on('payment_methods')
            table.integer('status_charge_id').unsigned().nullable()
            table.foreign('status_charge_id').references('id').on('status_charges')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

        with self.schema.create('vouchers') as table:
            table.increments('id')
            table.float('price')
            table.integer('buyout_id').unsigned().nullable()
            table.foreign('buyout_id').references('id').on('buyouts')
            table.integer('product_id').unsigned().nullable()
            table.foreign('product_id').references('id').on('products')
            table.integer('stand_order_voucher_id').unsigned().nullable()
            table.foreign('stand_order_voucher_id').references('id').on('stand_order_vouchers')
            table.integer('status_voucher_id').unsigned().nullable()
            table.foreign('status_voucher_id').references('id').on('status_vouchers')
            table.integer('user_created').unsigned().nullable()
            table.foreign('user_created').references('id').on('users')
            table.timestamps()
            table.soft_deletes()

    def down(self):
        self.schema.drop('vouchers')
        self.schema.drop('charges')
        self.schema.drop('buyouts')
        self.schema.drop('stand_order_vouchers')
        self.schema.drop('stand_orders')
        self.schema.drop('status_stand_orders')
        self.schema.drop('status_vouchers')
        self.schema.drop('payment_methods')
        self.schema.drop('status_charges')
