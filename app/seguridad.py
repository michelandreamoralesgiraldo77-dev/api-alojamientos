from datetime import datetime, timedelta
from functools import wraps
import jwt
from flask import request, jsonify
from app import Config


def generar_token(usuario_id):
    payload = {
        "usuario_id": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=24),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")


def requiere_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        cabecera = request.headers.get("Authorization")
        
        if not cabecera:
            return jsonify({
                "exito": False,
                "mensaje": "Falta token"
            }), 401
        
        if not cabecera.startswith("Bearer "):
            return jsonify({
                "exito": False,
                "mensaje": "Formato de token inválido"
            }), 401
        
        try:
            token = cabecera.replace("Bearer ", "")
            datos = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            return f(datos["usuario_id"], *args, **kwargs)
            
        except jwt.ExpiredSignatureError:
            return jsonify({
                "exito": False,
                "mensaje": "Token expirado"
            }), 401
            
        except jwt.InvalidTokenError:
            return jsonify({
                "exito": False,
                "mensaje": "Token inválido"
            }), 401
    
    return decorador