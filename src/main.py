from fastapi import FastAPI

app = FastAPI(title="Conteneurisation-Orchestration", description="Etl")

@app.get("/")
def read_root() -> dict:
    return {
        "statusCode": 200,
        "app": "Conteneurisation-Orchestration", 
        "endpoints": [""]
    }