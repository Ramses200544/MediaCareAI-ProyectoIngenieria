from pydantic import BaseModel, EmailStr

class DatosMedico(BaseModel):
    correo: EmailStr
    password: str
    