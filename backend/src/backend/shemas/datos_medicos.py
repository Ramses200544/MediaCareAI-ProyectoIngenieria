from pydantic import BaseModel, EmailStr, Field

class RegisterMedico(BaseModel): #Lo que se envía desde el Frontend
    name: str = Field(min_length=10, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

class ResponseMedico(BaseModel): #Lo que el backend responde
    id: int
    name: str = Field(min_length=10, max_length=100)
    email: EmailStr
