from fastapi import APIRouter, Depends, status 
from backend.pacientes.schemas.pacientes_schemas import CreatePatient, ResponsePatient
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.dependencies import get_current_medic
from backend.medicos.models.models_medico import MedicModel
from backend.pacientes.services.pacientes_service import PatientService

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/register", response_model=ResponsePatient, status_code=status.HTTP_201_CREATED, response_description="Usted registro a un paciente exitosamente")

def recibe_data_patient(patient: CreatePatient, db: Session = Depends(get_db), medic_id = int):

    new_patient = PatientService.verify_patient(patient = patient, db = db, medic_id = current_medic.id)
    
    return new_patient 
