from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.pacientes.repositories.pacientes_repository import PatientRepository
from backend.pacientes.models.models_pacientes import PatientModel
from backend.pacientes.schemas.pacientes_schemas import CreatePatient, ResponsePatient


class PatientService:

    @staticmethod
    def verify_patient(db: Session, patient: CreatePatient, medic_id: int) -> PatientModel:
        existing_patient = PatientRepository.get_patient_by_name(db, medic_id=medic_id, full_name=patient.full_name)
        if existing_patient:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El usuario ya existe dentro de MediaCare AI")

        new_patient = PatientRepository.create_patient(db=db, patient=patient, medic_id=medic_id)

        return new_patient

    



