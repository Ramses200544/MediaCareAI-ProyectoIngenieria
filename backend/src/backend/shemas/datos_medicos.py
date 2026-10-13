from pydantic import BaseModel, EmailStr

class DatosMedico(BaseModel):
    correo: EmailStr
    password: src = Field(min_length=8)
    