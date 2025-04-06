from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate  # 👈 Importa Migrate
from app.config.settings import Config
from app.models import db, init_app as init_db  # 👈 Importa `db` aquí
from app.routes import init_app as init_routes

migrate = Migrate()  # 👈 Crea una instancia global de Migrate

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Cargar configuración desde clase Config
    app.config.from_object(Config)

    # Inicializar base de datos
    init_db(app)

    # Inicializar migraciones
    migrate.init_app(app, db)  # 👈 Conecta migrate con app y db

    # Registrar rutas
    init_routes(app)

    return app

