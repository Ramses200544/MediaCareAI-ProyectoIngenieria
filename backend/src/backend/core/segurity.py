import bcrypt

def hash_password(password:str) -> str:
    hashed = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
    return hashed.decode()

def verify_password(password:str, hashed_password:str) -> bool:
    return bcrypt.checkpw(
        password.encode("UTF-8"),
        hashed_password("UTF-8"),
    )

prueba = hash_password("HolaXD453@4")
print(prueba)

prueba_1 = verify_password()

