from fastapi import APIRouter
from src.etl.extract import extract
from src.core.constants import HTTP_RESPONSE_KO, HTTP_RESPONSE_OK

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/")
async def start_etl():
    etl_steps = [
        ("extract", extract),
        #("transform", transform),
        #("load", load)
    ]
    
    response_list = []
    for step_name, step_func in etl_steps:
        try:
            step_func()
            response_list.append(HTTP_RESPONSE_OK(step_name))
        except Exception as e:
            response_list.append(HTTP_RESPONSE_KO(step_name, e))
    
    return response_list