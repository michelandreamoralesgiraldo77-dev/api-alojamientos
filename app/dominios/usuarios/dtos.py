from marshmallow import Schema, fields, validate, validates, ValidationError

class UsuarioDTO(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    correo = fields.Email(required=True)
    es_administrador = fields.Bool(dump_only=True)
    creado_en = fields.DateTime(dump_only=True)

class RegistroDTO(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    correo = fields.Email(required=True)
    contraseña = fields.Str(required=True, validate=validate.Length(min=6))
    
    @validates("nombre")
    def validar_nombre(self, value):
        if not value.strip():
            raise ValidationError("El nombre no puede estar vacío")

class LoginDTO(Schema):
    correo = fields.Email(required=True)
    contraseña = fields.Str(required=True)