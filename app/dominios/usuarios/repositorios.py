from typing import Optional, List
from app import db
from .modelos import Usuario

class RepositorioUsuarios:
    @staticmethod
    def crear(usuario: Usuario) -> Usuario:
        db.session.add(usuario)
        db.session.commit()
        return usuario
    
    @staticmethod
    def buscar_por_id(usuario_id: int) -> Optional[Usuario]:
        return Usuario.query.get(usuario_id)
    
    @staticmethod
    def buscar_por_correo(correo: str) -> Optional[Usuario]:
        return Usuario.query.filter_by(correo=correo).first()
    
    @staticmethod
    def listar_todos() -> List[Usuario]:
        return Usuario.query.all()