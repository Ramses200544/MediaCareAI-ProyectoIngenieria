from sqlalchemy import DateTime, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from backend.core.database import Base

class MedicModel(Base):
    __tablename__ = "medics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(150),nullable=False, unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255),nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255),nullable=False)
    speciality: Mapped[str] = mapped_column(String(100),nullable=True)
    is_activate: Mapped[bool] = mapped_column(Boolean, default=True)
    create_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    

