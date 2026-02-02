from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.src.api.v1.dataset.get_dataset import router as dataset_route
from backend.src.api.v1.etl.extract import router as extract_route

app = FastAPI(title="Conteneurisation-Orchestration", description="Etl", docs_url="/api/v1/swagger")
app.mount("/docs", StaticFiles(directory="documentation/site", html=True), name="docs")
app.include_router(dataset_route)
app.include_router(extract_route)

@app.get("/")
def read_root() -> dict:
    return {
        "statusCode": 200,
        "app": "Conteneurisation-Orchestration", 
        "endpoints": {
            "/api/v1/etl": {
                "/api/v1/etl/extract": "extract the dataset"
            },
            "documentation": {
                "/docs": "Documentation of the project",
                "/api/v1/swagger": "Swagger-ui documentation"
            },
            "/api/v1/dataset": "get the dataset"
        }
    }