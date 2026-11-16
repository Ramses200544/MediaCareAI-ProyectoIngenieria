from fastapi import FastAPI
from backend.medicos.routers.medico_router import router as router_medico
from backend.pacientes.routers.pacientes_routers import router as router_paciente

app = FastAPI(title="MediaCare AI", 
description= "Sistema de Backend para MediaCare AI",
version="1.0.0")

app.include_router(router_medico)
app.include_router(router_paciente)

@app.get("/")
def welcome():
    return {"message": ("Bienvenido a la primera versión de MediaCare AI")}















