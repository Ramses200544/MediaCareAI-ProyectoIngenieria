from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.segurity import decode_access_token
from backend.medicos.repositories.medico_repository import get_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/medics/login")




