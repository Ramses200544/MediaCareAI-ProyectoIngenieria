from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.medicos.schemas.medico_shema import MedicCreate, MedicResponse
from backend.medicos.schemas.medico_login import MedicLogin
from backend.medicos.services.medico_service import MedicService
from backend.core.database import get_db

router = APIRouter(prefix="/medics", tags=["medicos"])

@router.post("/register", response_model = MedicResponse, status_code=status.HTTP_201_CREATED, response_description="Usted se registro exitosamente")

def register_new_medic(medic: MedicCreate, db: Session = Depends(get_db)):

    new_medic = MedicService.register_medic(db=db, medic=medic)
    return new_medic

@router.post("/login", status_code=status.HTTP_200_OK, response_description="Usted accedio exitosamente")

def login(data_medic: MedicLogin, db: Session = Depends(get_db)):

    verify_medic = MedicService.authenticate_medic(db=db, data_medic=data_medic)

    return verify_medic






    
        


