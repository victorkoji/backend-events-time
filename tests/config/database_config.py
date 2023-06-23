import os

from orator import DatabaseManager, Model
from dotenv import load_dotenv

load_dotenv('.env.development')

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': os.getenv('DB_TEST_HOST', 'test_database'),
        'database': 'test_database',
        'user': 'postgres',
        'password': 'postgres',
        'port': 5432
    }
}

database = DatabaseManager(DATABASES)
Model.set_connection_resolver(database)
