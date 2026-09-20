class ErrorRecursoNoEncontrado(Exception):
    def __init__(self, mensaje="Recurso no encontrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorValidacion(Exception):
    def __init__(self, mensaje="Datos inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def manejo_errores(app):
    @app.errorhandler(ErrorRecursoNoEncontrado)
    def recurso_no_encontrado(e):
        return {"error": e.mensaje}, 404

    @app.errorhandler(ErrorValidacion)
    def error_validacion(e):
        return {"error": e.mensaje}, 400