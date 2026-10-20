from fastapi import FastAPI
from backend.medicos.routers import medico_router as router_medicos

app = FastAPI(title="MediaCareAI")

app.include_router(router_medicos.router)







