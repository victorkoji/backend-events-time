from orator.seeds import Seeder


class DatabaseSeeder(Seeder):

    def run(self):
        self.db.table('users').insert({
            'first_name': 'admin',
            'last_name': '',
            'birth_date': '2023-07-10',
            'email': 'admin@admin.com',
            'cellphone': '',
            'password': '$2b$12$FqYd6qWfqNZksbp5nVwjmu3UmbP2gPc55oF2FFalnx4kgX/8tKaiK',
        })
