from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.segurity import decode_access_token
from backend.medicos.repositories.medico_repository import MedicRepository
import jwt

oauth2_scheme = HTTPBearer()

def get_current_medic(
    credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = decode_access_token(token)
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar correctamente las credenciales",
            headers={"WWW-Authenticate": "Bearer"}
        )

    medic_id = payload.get("sub")
    
    if medic_id is None:
        raise HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail= "No se pudieron validar correctamente las credenciales",
         headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        medic_id = int(medic_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "No se pudieron validar correctamente las credenciales",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    
    current_medic = MedicRepository.get_by_id(db, medic_id)

    if current_medic is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "No se pudieron verificar correctamente las credenciales",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    
    if not current_medic.is_activate:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = "El médico se encuentra desactivado por el momento",
        )

    return current_medic
    





