from fastapi import APIRouter

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/extract")
def run_extract():
    pass