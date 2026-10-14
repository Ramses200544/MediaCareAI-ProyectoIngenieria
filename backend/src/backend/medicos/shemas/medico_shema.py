from pydantic import BaseModel, EmailStr, Field

class RegisterMedico(BaseModel):
    name: str = Field(min_length=10, max_length=80)
    email: EmailStr
    password: str

class ResponseMedico(BaseModel):
    id: int
    name: str = Field(max_length=10, max_length= 80)
    email: EmailStr
    