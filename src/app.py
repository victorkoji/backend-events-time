from flask import Flask
from controllers.product_controller import product_routes
from src.config.database import db

# Criar o aplicativo Flask
app = Flask(__name__)

# Definir configurações do Flask
app.config['DEBUG'] = True

# Registrar a blueprint no aplicativo Flask
app.register_blueprint(product_routes)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

# Executar o aplicativo Flask
if __name__ == '__main__':
    # Definir a variável de ambiente FLASK_ENV como "development"
    # os.environ['FLASK_ENV'] = 'development'
    print("server running")
    app.run()
