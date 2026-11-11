from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.segurity import decode_access_token
from backend.medicos.repositories.medico_repository import MedicRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/medics/login")

def get_current_medic(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)
    medic_id = payload.get("sub")

if medic_id is None:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "No se pudieron validar correctamente las credenciales",
        headers={"WWW-Authenticate": "Bearer"}
    )
    

    




