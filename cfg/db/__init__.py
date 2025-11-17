__version__ = "2.2"
__description__ = "Package to handle database"

from .classes.connect import ConnectDb
from db import ConnectDb

__all__ = ['ConnectDb']