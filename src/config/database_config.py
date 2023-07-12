import os

from orator import DatabaseManager, Model
from dotenv import load_dotenv

load_dotenv('.env.development')

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': os.getenv('DB_HOST', 'database'),
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        'port': 5432
    }
}

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)
