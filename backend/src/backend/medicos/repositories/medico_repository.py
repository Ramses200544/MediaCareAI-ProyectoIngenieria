from sqlalchemy.orm import Session
from backend.medicos.models.models_medico import MedicModel
from backend.medicos.schemas.medico_shema import MedicCreate

class MedicRepository:
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> MedicModel | None:
        """Se realiza una consulta en la BD para buscar si el correo existe"""
        return db.query(MedicModel).filter(MedicModel.email == email).first()
    
    @staticmethod
    def create_medic(db:Session, medic:MedicCreate, hashed_password:str) -> MedicModel:
        """Registramos los datos del schemas mediante la tabla medics de la BD"""
        db_medic = MedicModel(

           full_name=medic.full_name,
           email=medic.email,
           hashed_password=hashed_password,
           speciality=medic.speciality,

        )

        db.add(db_medic) #Preparamos el objeto que se va a registrar en la tabla
        db.commit() #Guarda con cambios dentro de la BD
        db.refresh(db_medic) #Actualiza la BD para visualizar 
        return db_medic

    @staticmethod
    def get_by_id(db: Session, medic_id: int) -> MedicModel | None:
        return db.query(MedicModel).filter(MedicModel.id == medic_id).first()
        
    






        

