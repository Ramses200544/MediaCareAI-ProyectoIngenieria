from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend.medicos.schemas.medico_shema import MedicCreate, MedicResponse
from backend.medicos.services.medico_service import MedicService
from backend.core.database import get_db

router = APIRouter(prefix="/medics", tags=["medicos"])

@router.post("/register", response_model = MedicResponse, status_code=status.HTTP_201_CREATED)

def register_new_medic(medic: MedicCreate, db: Session = Depends(get_db)):
    """Registrar a un nuevo medico dentro de la plataforma"""

    new_medic = MedicService.register_medic(db=db, medic=medic)
    return new_medic
    

    
        


