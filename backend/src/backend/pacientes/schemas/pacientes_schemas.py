from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

class CreatePatient(BaseModel):
    full_name: str = Field(min_length=2, max_length=80)
    date_birthday: date
    sex: Literal["Hombre", "Mujer"]
    antecedents: Optional[str] = None
    allergys: Optional[str] = None

class ResponsePatient(BaseModel):
    id: int
    full_name: str
    date_birthday: date
    sex: str
    antecedents: Optional[str] = None
    allergys: Optional[str] = None

model_conf = {"from_attributes":True}
