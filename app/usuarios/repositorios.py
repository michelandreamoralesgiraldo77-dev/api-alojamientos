from .modelos import db, Usuario

class UsuarioRepositorio:
    @staticmethod
    def obtener_todos():
        return Usuario.query.all()

    @staticmethod
    def obtener_por_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def obtener_por_correo(correo):
        return Usuario.query.filter_by(correo=correo).first()

    @staticmethod
    def crear(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def eliminar(usuario):
        db.session.delete(usuario)
        db.session.commit()