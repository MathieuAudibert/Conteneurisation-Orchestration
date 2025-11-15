__version__ = "2.1"
__description__ = "Package to handle database"

# FIXME: refactor ConnectDb and ConnectDbAdm les classes sont pareilles la chose qui differe c la variable d'env...

from .classes.connect.connectAdmin import ConnectDbAdm
from .classes.connect.connect import ConnectDb
from db import ConnectDbAdm, ConnectDb

__all__ = ['ConnectDbAdm', 'ConnectDb']