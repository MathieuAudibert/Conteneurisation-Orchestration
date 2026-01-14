from fastapi import FastAPI
from src.api.v1.dataset.get_dataset import router as dataset_route
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Conteneurisation-Orchestration", description="Etl", docs_url="/api/documentation")
app.include_router(dataset_route)
app.mount("/docs", StaticFiles(directory=".github/site", html=True), name="docs")

@app.get("/")
def read_root() -> dict:
    return {
        "statusCode": 200,
        "app": "Conteneurisation-Orchestration", 
        "endpoints": {
            "/docs": "Documentation of the project",
            "/api/documentation": "Swagger-ui documentation",
            "/dataset": "get the dataset"
        }
    }