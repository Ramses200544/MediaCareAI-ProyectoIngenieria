class EmailAlreadyRegisterError(Exception):
    """se intento registrar un email que ya existe dentro de los registros"""

class UserNotFoundError(Exception):
    """No existe el usuario que desea encontrar"""

    