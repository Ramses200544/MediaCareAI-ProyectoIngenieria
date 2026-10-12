from pydantic import BaseModel, EmailStr

class DatosMedico(BaseModel):
    correo: EmailStr
    password: Field(min_length=8)
    