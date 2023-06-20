from flask import Flask
from controllers.product_controller import ProductController
from orator import DatabaseManager, Model
from config.database import database

# Criar o aplicativo Flask
app = Flask(__name__)

product_controller = ProductController(app)


@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == '__main__':
    app.db = database
    app.run(debug=True)
