from pydantic import BaseModel, EmailStr, Field

class MedicBase(BaseModel):
    full_name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    speciality: str | None = Field(min_length=3, max_length=100)

class MedicCreate(MedicBase):
    password: str = Field(min_length=8, max_length=255)

class MedicResponse(MedicBase):
    id: int
    is_activate: bool

    model_config =  { #Permite que Pydantic lee directamente de SQLAlchemy
      "from_attributes": True
    }



    
        




    
    