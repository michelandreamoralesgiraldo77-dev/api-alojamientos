class ApiError(Exception):
    codigo: int
    mensaje: str
    
    def __init__(self, codigo: int, mensaje: str):
        super().__init__(mensaje)
        self.codigo = codigo
        self.mensaje = mensaje