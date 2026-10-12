from fastapi import APIRouter, HTTPException
from backend.shemas.datos_medicos import DatosMedico

router = APIRouter(prefix="/Usuarios", tags=["Medicos"])

@router.post("/medicos", status_code=201)
def recibir_datos(medico: DatosMedico):
    return {"mensaje": "registro exitoso"}
