import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.core.configure import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Comprobar que exista la DB
print("Existe la BD:", bool(settings.DATABASE_URL))

#Comprobar si utiliza PostgresSQL
print("¿Utiliza PostgreSQL?:", settings.DATABASE_URL.startswith("postgresql"))
        