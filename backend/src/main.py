from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.v1.dataset.get_dataset import router as dataset_route
from backend.src.api.v1.etl.extract import router as extract_route
from backend.src.api.v1.etl.transform import router as transform_route
from backend.src.api.v1.etl.load import router as load_route
from backend.src.api.v1.etl.workflow import router as workflow_route
from backend.src.api.v1.data.get_cars import router as cars_route
from backend.src.api.v1.data.get_logs import router as logs_route

app = FastAPI(title="Conteneurisation-Orchestration", description="Etl", docs_url="/api/v1/swagger")
app.add_middleware(    
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/docs", StaticFiles(directory="documentation/site", html=True), name="docs")
app.include_router(dataset_route)
app.include_router(extract_route)
app.include_router(transform_route)
app.include_router(load_route)
app.include_router(workflow_route)
app.include_router(cars_route)
app.include_router(logs_route)

@app.get("/")
def read_root() -> dict:
    return {
        "statusCode": 200,
        "app": "Conteneurisation-Orchestration", 
        "endpoints": {
            "/api/v1/etl": {
                "/extract": "extract the dataset",
                "/transform": "transform the dataset",
                "/load": "load the dataset into MongoDB",
                "/workflow": "run the complete ETL pipeline (Extract -> Transform -> Load)"
            },
            "/api/v1/data": {
                "/cars": "get cars and stats about it",
                "/logs": "get logs and stats about it"
            },
            "documentation": {
                "/docs": "Documentation of the project",
                "/api/v1/swagger": "Swagger-ui documentation"
            },
            "/api/v1/dataset": "get the dataset"
        }
    }