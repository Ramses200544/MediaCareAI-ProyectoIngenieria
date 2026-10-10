from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def funcion_prueba():
    return {"Hola": "Asistente de MediaCare AI Funcionando"}
