import os

from orator import DatabaseManager, Model
from dotenv import load_dotenv

if os.getenv("FLASK_ENV") == 'development':
    load_dotenv(dotenv_path=f'.env.{os.getenv("FLASK_ENV")}')

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': 5432
    }
}

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)
