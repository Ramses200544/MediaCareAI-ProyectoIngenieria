import string, bcrypt

def validar_password(password: str) -> bool:
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True

def encriptar_password(password:str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def registrar_medico(medico):
    if not validar_password(password.medico):
        raise ContrasenaInvalidaError()
    

    
