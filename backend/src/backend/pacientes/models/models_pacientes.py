from sqlalchemy import (String, Integer, Date, Text, DateTime, ForeignKey)
from datetime import date
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from backend.core.database import Base
from typing import Optional

class PatientModel(Base):
    __tablename__= "patients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    medic_id: Mapped[int] = mapped_column(Integer, ForeignKey("medics.id"), index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(80), nullable=False)
    date_birthday: Mapped[date] = mapped_column(Date, nullable=False)
    sex: Mapped[str] = mapped_column(String(10), nullable=False)
    antecedents: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    allergys: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    date_register : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    