import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import crear_app
from app import db

@pytest.fixture
def cliente():
    config_pruebas = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "SECRET_KEY": "prueba_clave_segura",
        "JWT_EXP_MINUTES": 15
    }
    
    app = crear_app(config_pruebas)
    
    with app.test_client() as cliente:
        with app.app_context():
            db.create_all()
            yield cliente
            db.drop_all()