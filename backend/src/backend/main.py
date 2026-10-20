from fastapi import FastAPI
from src.backend.routers import medico_router

app = FastAPI(title="MediaCareAI")

app.include_router(medico_router.router)







