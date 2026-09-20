import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest 
from app import crear_app
from app.__init__ import db

@pytest.fixture
def cliente():
    app = crear_app()
    app.config.update({"TESTING": True})
    
    with app.test_client() as cliente:
        with app.app_context():
            yield cliente