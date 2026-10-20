from sqlalchemy.orm import Mapped, mapped_column
from backend.core.database import Base

class User(Base):
    __tablename__: "users"
    id_medico: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique = True, index = True)
    hashed_password[str]



