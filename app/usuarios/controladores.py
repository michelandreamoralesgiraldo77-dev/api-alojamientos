from flask import jsonify, request
from .dtos import UsuarioCrear, UsuarioRespuesta
from .servicios import UsuarioServicio
from app.dominios.seguridad import requiere_token

class UsuarioControlador:
    @staticmethod
    def listar():
        usuarios = UsuarioServicio.listar_usuarios()
        return jsonify([UsuarioRespuesta.desde_modelo(u) for u in usuarios])

    @staticmethod
    def obtener(usuario_id):
        usuario = UsuarioServicio.obtener_usuario(usuario_id)
        return jsonify(UsuarioRespuesta.desde_modelo(usuario))

    @staticmethod
    def registrar():
        datos = request.get_json()
        dto = UsuarioCrear(datos)
        usuario = UsuarioServicio.registrar_usuario(dto)
        return jsonify(UsuarioRespuesta.desde_modelo(usuario)), 201