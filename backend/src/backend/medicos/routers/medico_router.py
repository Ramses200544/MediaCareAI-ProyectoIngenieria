from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from backend.medicos.shemas.medico_shema import RegisterMedico, ResponseMedico


router = APIRouter(prefix="/medicos", tags["medicos"])

@router.post("")