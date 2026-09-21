from typing import List, Optional
from .modelos import Usuario
from .repositorios import RepositorioUsuarios
from app.seguridad import generar_token

class ServicioUsuarios:
    @staticmethod
    def registrar(nombre: str, correo: str, contraseña: str) -> Usuario:
        if RepositorioUsuarios.buscar_por_correo(correo):
            raise ValueError("El correo ya está registrado")
        usuario = Usuario(nombre=nombre, correo=correo)
        usuario.contraseña = contraseña
        return RepositorioUsuarios.crear(usuario)
    
    @staticmethod
    def iniciar_sesion(correo: str, contraseña: str) -> Optional[str]:
        usuario = RepositorioUsuarios.buscar_por_correo(correo)
        if not usuario or not usuario.verificar_contraseña(contraseña):
            raise ValueError("Credenciales inválidas")
        return generar_token(usuario.id)
    
    @staticmethod
    def obtener_por_id(usuario_id: int) -> Optional[Usuario]:
        return RepositorioUsuarios.buscar_por_id(usuario_id)
    
    @staticmethod
    def listar() -> List[Usuario]:
        return RepositorioUsuarios.listar_todos()