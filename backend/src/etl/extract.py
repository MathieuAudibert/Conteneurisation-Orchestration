from pathlib import Path
import os
import sys
import pandas as pd

try:
    from .log_config import get_logger
except Exception:
    _here = Path(__file__).resolve()
    project_root = _here.parents[2]
    src_dir = project_root / "src"
    if src_dir.exists():
        sys.path.insert(0, str(src_dir))
    else:
        sys.path.insert(0, str(project_root))

    try:
        from src.etl.log_config import get_logger
    except Exception:
        try:
            from log_config import get_logger
        except Exception:
            raise

logger = get_logger(__name__)

def _resolve_path(file_path):
    p = Path(file_path)
    if p.is_absolute():
        return p

    data_dir = os.environ.get("DATA_DIR")
    if data_dir:
        return (Path(data_dir) / file_path).resolve()

    project_root = Path(__file__).resolve().parents[2]

    fp = Path(file_path)
    if fp.parts and fp.parts[0].lower() == "cfg":
        repo_cfg_candidate = project_root.parent / fp
        if repo_cfg_candidate.exists():
            return repo_cfg_candidate.resolve()
        return (project_root / fp).resolve()
    else:
        repo_cfg_candidate = project_root.parent / "cfg" / fp  
        if repo_cfg_candidate.exists():
            return repo_cfg_candidate.resolve()
        return (project_root / "cfg" / fp).resolve()


def extract(file_path):
    logger.info(f"[INFO]: Début de l'extraction des données depuis {file_path}")
    try:
        path = _resolve_path(file_path)
        logger.debug(f"[INFO]: Chemin résolu pour l'extraction : {path}")
        cars = pd.read_csv(path)
        logger.info(f"[INFO]: Extraction réussie : {len(cars)} lignes extraites.")
        return cars
    except Exception as e:
        logger.error(f"[ERROR]: Erreur lors de l'extraction des données depuis {file_path} : {e}")
        raise


if __name__ == "__main__":
    default_file = os.environ.get("DEFAULT_FILE", "dataset-cars-dirty.csv")
    cars = extract(default_file)
    print(cars.head())