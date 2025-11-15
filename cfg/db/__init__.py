__version__ = "2.0"
__description__ = "Package to handle database"

from .classes.connect.connectAdmin import ConnectDbAdm
# from .classes.connect.connect import ConnectDb
from db import ConnectDbAdm

__all__ = ['ConnectDbAdm']