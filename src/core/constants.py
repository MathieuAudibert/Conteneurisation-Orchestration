from pathlib import Path

HTTP_RESPONSE_OK= lambda type: {
    "status": 200,
    "message": f"{type} SUCCESS"
}

HTTP_RESPONSE_KO= lambda type, e: {
    "status": 500,
    "message": f"{type} FAILED - {str(e)}"
}

BASE_DIR=Path(__file__).resolve().parent.parent