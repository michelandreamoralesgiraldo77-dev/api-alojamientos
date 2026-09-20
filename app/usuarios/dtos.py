class UsuarioCrear:
    def __init__(self, datos):
        self.nombre = datos.get("nombre")
        self.correo = datos.get("correo")
        self.contraseña = datos.get("contraseña")

    def validar(self):
        errores = []
        if not self.nombre or len(self.nombre.strip()) < 3:
            errores.append("El nombre debe tener al menos 3 caracteres")
        if not self.correo or "@" not in self.correo:
            errores.append("El correo no es válido")
        if not self.contraseña or len(self.contraseña) < 6:
            errores.append("La contraseña debe tener al menos 6 caracteres")
        return errores

class UsuarioRespuesta:
    @staticmethod
    def desde_modelo(usuario):
        return {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "es_admin": usuario.es_admin
        }