__version__ = "2.2"
__description__ = "Module qui gere la bdd"

from .classes.connect import ConnectDB
from db import ConnectDB

__all__ = ['ConnectDB']