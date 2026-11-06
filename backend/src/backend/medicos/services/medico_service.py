from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.medicos.schemas.medico_shema import MedicCreate
from backend.medicos.schemas.medico_login import MedicLogin
from backend.medicos.repositories.medico_repository import MedicRepository
from backend.medicos.models.models_medico import MedicModel 
from backend.core.password import get_password, verify_password
from backend.core.segurity import create_access_token

class MedicService:

    #Método para verificar si un correo ya se encuentra registrado
    @staticmethod
    def register_medic(db:Session, medic:MedicCreate) -> MedicModel:

        existing_email_register = MedicRepository.get_by_email(db, email=medic.email)
        if existing_email_register:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El correo ya esta registrado en el sistema MediaCare AI")

        hw_password = get_password(medic.password)

        new_medic = MedicRepository.create_medic(db=db, medic=medic, hashed_password=hw_password)

        return new_medic
    
    @staticmethod
    def authenticate_medic(db:Session, data_medic: MedicLogin) -> MedicModel:

        medic = MedicRepository.get_by_email(db, email=data_medic.email)

        if not medic:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="correo o contraseña incorrectos")
        
        if not verify_password(data_medic.password, medic.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="correo o contraseña incorrectos")


        access_token = create_access_token(
            data={"sub": medic.email}
        )

        return {

            "access_token": access_token,
            "token_type": "bearer",
        }

      


    
            

