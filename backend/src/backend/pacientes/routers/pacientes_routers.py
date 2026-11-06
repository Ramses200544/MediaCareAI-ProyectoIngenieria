from fastapi import APIRouter, Depends, status, HTTPException
from backend.pacientes.schemas.pacientes_schemas import CreatePatient, ResponsePatient
from sqlalchemy.orm import Session
from backend.core.database import get_db

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/register", response_model=ResponsePatient, status_code=status.HTTP_201_CREATED, response_description="Usted registro a un paciente exitosamente")

def recibe_data_patient(patient: CreatePatient, db: Session = Depends(get_db)):
    pass
