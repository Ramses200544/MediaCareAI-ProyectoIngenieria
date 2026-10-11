from fastapi import FastAPI

app = FastAPI(
    Title="MediaCare AI"
)

@app.get("/")
def hola():
    return {"Hola": "mundo"}
    