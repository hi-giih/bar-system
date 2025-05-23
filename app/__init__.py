from flask import Flask
from app.banco.database import db

from app.rotas.clientes_rota import cliente_rt

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "your-secret_key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    app.register_blueprint(cliente_rt)

    return app
