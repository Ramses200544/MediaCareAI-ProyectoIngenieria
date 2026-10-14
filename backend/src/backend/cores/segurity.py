from passlib.context import CryptContext

pwt_context = CryptContext(shemes["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwt_context.verify(plain_password, hashed_password)

   