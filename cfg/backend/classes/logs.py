from dataclasses import dataclass
from datetime import datetime

@dataclass
class Logs:
    __created_at: datetime.now()
    __timestamp: datetime.now()
    _user_id: int
    _action: str
    _metadata: str
    
    def __post_init__(self):
        self.created_at = self.__created_at
        self.timestamp = self.__timestamp
        self.user_id = self._user_id
        self.action = self._action

    # le code suivant sert a s'assurer que les champs soient du bon type 
    # en gros : si user_id.type = str --> ERREUR

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def action(self):
        return self._action

    @property
    def metadata(self):
        return self._metadata
    
    @user_id.setter
    def user_id(self, value:int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: user_id must be int")
        self._user_id = value
    
    @action.setter
    def action(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: action must be str")
        self._action = value
    
    @metadata.setter
    def metadata(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: metadata must be str")
        self._metadata = value

