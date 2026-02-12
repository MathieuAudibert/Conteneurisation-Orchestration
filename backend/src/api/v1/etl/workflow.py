from typing import Any
from fastapi import APIRouter
from backend.src.etl.extract import extract
from backend.src.etl.transform import transform_cars
from backend.src.core.db.doctrine import Doctrine
from backend.src.core.logger import get_logger
import pandas as pd
from pathlib import Path

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])
logger = get_logger(__name__)

@router.get("/workflow")
def run_workflow() -> dict[str, Any]:
    try:
        logger.info("Starting ETL workflow - Extract phase")
        project_root = Path(__file__).parent.parent.parent.parent.parent.parent
        csv_path = project_root / "cfg" / "dataset-cars-dirty.csv"
        cars = extract(str(csv_path))
        
        if not cars:
            return {
                "statusCode": 400,
                "message": "No data extracted"
            }
        
        cars_data = []
        for car in cars:
            car_dict = {
                'brand': car.brand,
                'model': car.model,
                'full_model_name': car.full_model_name,
                'transmission': car.transmission.name,
                'fuel_type': car.fuel_type.name,
                'make_year': car.make_year,
                'reg_year': car.reg_year,
                'engine_capacity_cc': car.engine_capacity_cc,
                'engine_category': car.engine_category,
                'km_driven': car.km_driven,
                'usage_category': car.usage_category,
                'ownership': car.ownership,
                'ownership_category': car.ownership_category,
                'price': car.price,
                'overall_cost': car.overall_cost,
                'total_value': car.total_value,
                'price_category': car.price_category,
                'has_insurance': car.has_insurance,
                'spare_key': car.spare_key,
                'ready_for_sale': car.ready_for_sale,
                'reg_number': car.reg_number,
                'title': car.title,
                'age_of_car': car.age_of_car,
                'usage_efficency': car.usage_efficency,
                'is_old_car': car.is_old_car,
                'is_expensive': car.is_expensive,
                'well_maintened': car.well_maintened,
                'economy_score': car.economy_score
            }
            cars_data.append(car_dict)
        
        df = pd.DataFrame(cars_data)
        logger.info(f"Extract complete - {len(cars)} records extracted")
        
        # transform
        logger.info("Starting Transform phase")
        df_transformed = transform_cars(df, logger=logger)
        logger.info(f"Transform complete - {len(df_transformed)} records transformed")
        
        # load
        logger.info("Starting Load phase")
        data = df_transformed.to_dict(orient='records')
        
        doctrine = Doctrine()
        
        deleted_count = doctrine.delete('cars', {}, many=True)
        logger.info(f"Cleared {deleted_count} existing records from cars collection")
        
        inserted_ids = doctrine.insert('cars', data)
        inserted_count = len(inserted_ids) if isinstance(inserted_ids, list) else 1
        logger.info(f"Load complete - {inserted_count} records inserted")
        
        return {
            "statusCode": 200,
            "message": "ETL workflow completed successfully",
            "extract": {
                "records_extracted": len(cars)
            },
            "transform": {
                "records_transformed": len(df_transformed),
                "columns": list(df_transformed.columns)
            },
            "load": {
                "records_deleted": deleted_count,
                "records_inserted": inserted_count
            }
        }
    except Exception as e:
        logger.error(f"Error during ETL workflow: {e}")
        return {
            "statusCode": 500,
            "message": f"Error during ETL workflow: {str(e)}"
        }