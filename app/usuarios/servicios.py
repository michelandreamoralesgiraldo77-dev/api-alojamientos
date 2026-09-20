from .modelos import Usuario
from .repositorios import UsuarioRepositorio
from app.dominios.errores import ErrorValidacion, ErrorRecursoNoEncontrado
import hashlib

class UsuarioServicio:
    @staticmethod
    def listar_usuarios():
        return UsuarioRepositorio.obtener_todos()

    @staticmethod
    def obtener_usuario(usuario_id):
        usuario = UsuarioRepositorio.obtener_por_id(usuario_id)
        if not usuario:
            raise ErrorRecursoNoEncontrado("Usuario no existe")
        return usuario

    @staticmethod
    def registrar_usuario(datos_dto):
        errores = datos_dto.validar()
        if errores:
            raise ErrorValidacion(", ".join(errores))

        if UsuarioRepositorio.obtener_por_correo(datos_dto.correo):
            raise ErrorValidacion("El correo ya está registrado")

        contraseña_cifrada = hashlib.sha256(datos_dto.contraseña.encode()).hexdigest()
        
        nuevo = Usuario(
            nombre=datos_dto.nombre,
            correo=datos_dto.correo,
            contraseña=contraseña_cifrada
        )
        return UsuarioRepositorio.crear(nuevo)