from flask import Blueprint, request, jsonify
from app import db
from app.dominios.usuarios.modelos import Usuario
from app.dominios.usuarios.dtos import UsuarioDTO, RegistroDTO, LoginDTO
from app.dominios.usuarios.servicios import ServicioUsuarios
from app.seguridad import generar_token, requiere_token

bp_usuarios = Blueprint("usuarios", __name__)
servicio_usuarios = ServicioUsuarios()

@bp_usuarios.route("/registro", methods=["POST"])
def registro():
    datos = request.get_json()
    dto = RegistroDTO()
    errores = dto.validate(datos)
    if errores:
        return jsonify({"exito": False, "mensaje": "Datos inválidos", "errores": errores}), 400
    try:
        usuario = servicio_usuarios.registrar(
            nombre=datos["nombre"],
            correo=datos["correo"],
            contraseña=datos["contraseña"]
        )
        return jsonify({"exito": True, "mensaje": "Usuario registrado", "datos": usuario.a_dto()}), 201
    except ValueError as e:
        return jsonify({"exito": False, "mensaje": str(e)}), 400

@bp_usuarios.route("/login", methods=["POST"])
def login():
    datos = request.get_json()
    dto = LoginDTO()
    errores = dto.validate(datos)
    if errores:
        return jsonify({"exito": False, "mensaje": "Datos inválidos", "errores": errores}), 400
    try:
        token = servicio_usuarios.iniciar_sesion(
            correo=datos["correo"],
            contraseña=datos["contraseña"]
        )
        return jsonify({"exito": True, "token": token}), 200
    except ValueError as e:
        return jsonify({"exito": False, "mensaje": str(e)}), 401

@bp_usuarios.route("/perfil", methods=["GET"])
@requiere_token
def perfil(usuario_id):
    usuario = servicio_usuarios.obtener_por_id(usuario_id)
    if not usuario:
        return jsonify({"exito": False, "mensaje": "Usuario no encontrado"}), 404
    return jsonify({"exito": True, "datos": usuario.a_dto()}), 200