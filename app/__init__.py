from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    
    @app.route("/health", methods=["GET"])
    def salud():
        return {
            "status": "ok",
            "service": "alojamientos-api",
            "version": "v1"
        }, 200
    
    return app