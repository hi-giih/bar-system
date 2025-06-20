from flask import Flask
from app.banco.database import db

from app.rotas.clientes_rota import cliente_rt
from app.rotas.produtos_rota import produto_rt
from app.rotas.comandas_rota import comanda_rt
from app.rotas.pagamentos_rota import pagamento_rt

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "your-secret_key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    app.register_blueprint(cliente_rt)
    app.register_blueprint(produto_rt)
    app.register_blueprint(comanda_rt)
    app.register_blueprint(pagamento_rt)

    return app
