from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.__init__ import db
from app.config import Config

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

app = crear_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)