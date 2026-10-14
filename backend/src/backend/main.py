from fastapi import FastAPI
from backend.routers.medicos import router as router_medicos

app = FastAPI(title="MediaCareAI")

app.include_router(router_medicos, prefix="/usuarios", tags=["medicos"])






