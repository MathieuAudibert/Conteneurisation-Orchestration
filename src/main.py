from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from src.etl.etl import router as start_etl_router
from src.core.constants import BASE_DIR

app = FastAPI(
    title="Conteneurisation-Orchestration", 
    description="ETL API for Conteneurisation-Orchestration",
    docs_url="/api-docs"
)
app.mount(
    "/docs", 
    StaticFiles(directory=BASE_DIR.parent / ".github" / "site", html=True), 
    name="zensical"
)
app.include_router(start_etl_router)

@app.exception_handler(Exception)
async def default_exception_handler(request: Request, e: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={e.__class__.__name__: str(e)})

@app.get("/")
def read_root():
    return {
        "app": "Conteneurisation-Orchestration",
        "endpoints": ["/etl", "/docs", "/api-docs"]
    }

