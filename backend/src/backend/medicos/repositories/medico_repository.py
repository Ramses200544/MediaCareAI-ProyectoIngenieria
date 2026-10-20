from sqlalchemy import Column, Integer, String
from backend.models.user import User

def create_user(db:Session, name:Str, email:str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

