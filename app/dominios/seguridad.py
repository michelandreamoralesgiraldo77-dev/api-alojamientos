from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta
from .config import Config

def generar_token(usuario_id):
    payload = {
        "usuario_id": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm="HS256")

def verificar_token(token):
    try:
        return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def requiere_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        encabezado = request.headers.get("Authorization")
        if not encabezado:
            return {"error": "Token requerido"}, 401
        
        partes = encabezado.split(" ")
        if len(partes) != 2 or partes[0] != "Bearer":
            return {"error": "Formato de token inválido"}, 401
        
        datos = verificar_token(partes[1])
        if not datos:
            return {"error": "Token inválido o expirado"}, 401
        
        request.usuario_id = datos["usuario_id"]
        return f(*args, **kwargs)
    return decorador