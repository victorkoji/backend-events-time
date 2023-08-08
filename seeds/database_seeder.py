import os

from orator.seeds import Seeder


class DatabaseSeeder(Seeder):

    def run(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(current_directory, 'initial_load.sql')

        with open(sql_file_path, mode='r', encoding="utf-8") as file:
            sql_script = file.read()

        self.db.statement(sql_script)
