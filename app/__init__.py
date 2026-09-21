from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()


class Config:
    SECRET_KEY = "tu-clave-secreta-super-segura-2026"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1093219367@localhost:3306/api_alojamientos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)


    from app.dominios.usuarios.controladores import bp_usuarios
    app.register_blueprint(bp_usuarios, url_prefix="/api/usuarios")

    @app.route("/health", methods=["GET"])
    def health():
        return {
            "status": "ok",
            "service": "alojamientos-api",
            "version": "v1"
        }, 200

    return app