from sqlalchemy.orm import Session
from backend.pacientes.models.models_pacientes import PatientModel
from backend.pacientes.schemas.pacientes_schemas import CreatePatient

class PatientRepository:

    @staticmethod
    def create_patient(db: Session, patient: CreatePatient, medic_id: int) -> PatientModel:
        new_patient = PatientModel(

            medic_id=medic_id, #Foreign Key
            full_name=patient.full_name,
            date_birthday=patient.date_birthday,
            sex=patient.sex,
            antecedents=patient.antecedents,
            allergys=patient.allergys,

        )
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)

        return new_patient

    @staticmethod
    def get_patient_by_name(db: Session, medic_id: int, full_name : str) -> PatientModel | None:
        return db.query(PatientModel).filter(PatientModel.medic_id == medic_id, PatientModel.full_name == full_name).first()

    @staticmethod
    def list_patients(db: Session, medic_id: int) -> list[PatientModel]:
        return db.query(PatientModel).filter(PatientModel.medic_id == medic_id).order_by(PatientModel.full_name).all()

    @staticmethod
    def get_patients_by_id(db: Session, medic_id: int, patient_id: int) -> PatientModel | None:
        return db.query(PatientModel).filter(PatientModel.id == patient_id, PatientModel.medic_id== medic_id).first()


