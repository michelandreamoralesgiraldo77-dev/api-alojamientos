from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from app.__init__ import db

load_dotenv()

def crear_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    Migrate(app, db)
    
    CORS(app)
    
    @app.route("/health", methods=["GET"])
    def salud():
        return {
            "status": "ok",
            "service": "alojamientos-api",
            "version": "1"
        }, 200
    
    return app

app = crear_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)