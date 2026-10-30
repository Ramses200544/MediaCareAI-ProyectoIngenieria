from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.medicos.schemas.medico_shema import MedicCreate
from backend.medicos.repositories.medico_repository import MedicRepository
from backend.medicos.models.models_medico import MedicModel 
from backend.core.segurity import get_password

class MedicService:

    #Método para verificar si un correo ya se encuentra registrado
    @staticmethod
    def register_medic(db:Session, medic:MedicCreate) -> MedicModel:
        existing_email_register = MedicRepository.get_by_email(db, email=medic.email)
        if existing_email_register:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya esta registrado en el sistema MediaCare AI")
      #Cifrar la contraseña de forma segura 
        hw_password = get_password(medic.password)

    #Registrar a un nuevo médico mediante repository
        new_medic = MedicRepository.create_medic(db=db, medic=medic, hashed_password=hw_password)

        return new_medic
      


    
            

