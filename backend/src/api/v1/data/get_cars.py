from fastapi import APIRouter, HTTPException
from backend.src.core.db.doctrine import Doctrine

router = APIRouter(prefix="/api/v1/data", tags=["data"])

@router.get("/cars")
def get_all_cars():# -> dict[str, Any]:
    try:
        doctrine = Doctrine()
        cars = doctrine.select_all("cars")
        for car in cars:
            if '_id' in car:
                car['_id'] = str(car['_id'])
        return {
            "statusCode": 200,
            "data": cars,
            "count": len(cars)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching cars: {str(e)}")

@router.get("/cars/stats")
def get_cars_stats():# -> dict[str, Any]:
    """Get statistics about cars"""
    try:
        doctrine = Doctrine()
        cars = doctrine.select_all("cars")
        
        total_cars = len(cars)
        avg_price = sum(car.get('price', 0) for car in cars) / total_cars if total_cars > 0 else 0
        
        return {
            "statusCode": 200,
            "data": {
                "total_cars": total_cars,
                "average_price": avg_price,
                "latest_cars": cars[-5:] if total_cars > 5 else cars
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching car stats: {str(e)}")
