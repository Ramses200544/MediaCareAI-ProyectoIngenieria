from fastapi import APIRouter, HTTPException, status
from backend.medicos.shemas import RegisterMedico, ResponseMedico

router = APIRouter(prefix="/usuarios", tags=["medicos"])

simulation_db = [{"id": 1, "full_name": "Ramses", "email":"ramses44@gmail.com"}, 
{"id": 2, "full_name": "Alondra", "email":"anitaalo12@gmail.com"}]

@router.get("")
def filter_list():
    return simulation_db

@router.get("/{user_id}") # GET USER/2
def search_user(user_id:int):
    for user in simulation_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, details="user no search")

@router.post("", status_code=201)
def create_user(data: Dict):
    new_user = {"id": len(simulation_db) + 1, **data}
    simulation_db.append(new_user)
    return new_user 
