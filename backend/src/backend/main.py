from fastapi import FastAPI
from backend.routers import medicos as router_medicos

app = FastAPI(title="MediaCare AI")

app.include_router(router_medicos.router)




