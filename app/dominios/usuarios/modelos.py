from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False, index=True)
    contraseña_hash = db.Column(db.String(255), nullable=False)
    es_administrador = db.Column(db.Boolean, default=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def contraseña(self):
        raise AttributeError("contraseña no es legible")
    
    @contraseña.setter
    def contraseña(self, contraseña: str):
        self.contraseña_hash = generate_password_hash(contraseña)
    
    def verificar_contraseña(self, contraseña: str) -> bool:
        return check_password_hash(self.contraseña_hash, contraseña)
    
    def a_dto(self):
        return {"id": self.id, "nombre": self.nombre, "correo": self.correo, "es_administrador": self.es_administrador, "creado_en": self.creado_en.isoformat()}