from sqlalchemy import create_engine
from sqlalchemy.org import DeclarativeBase, sessionmaker
from backend.core.configure import settings

engine = create_engine(settings.database_url, connect_args= {"check_same_theread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


