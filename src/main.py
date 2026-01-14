from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.api.v1.dataset.get_dataset import router as dataset_route
from src.api.v1.etl.load import router as load_route

app = FastAPI(title="Conteneurisation-Orchestration", description="Etl", docs_url="/api/documentation")
app.mount("/docs", StaticFiles(directory=".github/site", html=True), name="docs")
app.include_router(dataset_route)
app.include_router(load_route)

@app.get("/")
def read_root() -> dict:
    return {
        "statusCode": 200,
        "app": "Conteneurisation-Orchestration", 
        "endpoints": {
            "/etl": {
                "/etl/load": "load the dataset"
            },
            "/docs": "Documentation of the project",
            "/api/documentation": "Swagger-ui documentation",
            "/dataset": "get the dataset"
        }
    }