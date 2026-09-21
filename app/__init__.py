from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrar = Migrate()

def crear_app(configuracion=None):
    app = Flask(__name__)

    if configuracion:
        app.config.update(configuracion)
    else:
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        app.config["JWT_EXP_MINUTES"] = int(os.getenv("JWT_EXP_MINUTES", 15))
        
        usuario = os.getenv("DB_USUARIO")
        contrasena = os.getenv("DB_CONTRASENA")
        host = os.getenv("DB_HOST", "localhost")
        base = os.getenv("DB_NOMBRE")
        
        app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{usuario}:{contrasena}@{host}/{base}"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrar.init_app(app, db)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from app.rutas import bp as bp_salud
    app.register_blueprint(bp_salud)

    from app.dominios.usuarios.controladores import bp_usuarios
    app.register_blueprint(bp_usuarios, url_prefix="/api/v1/usuarios")

    return app