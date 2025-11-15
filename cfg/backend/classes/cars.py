from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TransmissionType(Enum):
    AUTOMATIC = 1
    MANUAL = 2

class FuelType(Enum):
    DIESEL = 1
    PETROL = 2
    HYBRID = 3

@dataclass
class Cars:
    __created_at: datetime.now()
    _brand: str
    _model: str
    _full_model_name: str
    _transmission: TransmissionType
    _fuel_type: FuelType
    _make_year: str
    _reg_year: str
    _engine_capacity_cc: int
    _engine_category: str
    _km_driven: int
    _usage_category: str
    _ownership: int
    _ownership_category: str
    _price: int
    _overall_cost: int
    _total_value: int
    _price_category: str
    _has_insurance: bool
    _spare_key: bool
    _ready_for_sale: bool
    _reg_number: str
    _title: str
    _age_of_car: int
    _usage_efficency: int
    _is_old_car: bool
    _is_expensive: bool
    _well_maintened: bool
    _economy_score: float

    def __post_init__(self):
        self.created_at = self.__created_at
        self.brand = self._brand
        self.model = self._model
        self.full_model_name = self._full_model_name
        self.transmission = self._transmission
        self.fuel_type = self._fuel_type
        self.make_year = self._make_year
        self.reg_year = self._reg_year
        self.engine_capacity_cc = self._engine_capacity_cc
        self.engine_category = self._engine_category
        self.km_driven = self._km_driven
        self.usage_category = self._usage_category
        self.ownership = self._ownership
        self.ownership_category = self._ownership_category
        self.price = self._price
        self.overall_cost = self._overall_cost
        self.total_value = self._total_value
        self.price_category = self._price_category
        self.has_insurance = self._has_insurance
        self.spare_key = self._spare_key
        self.ready_for_sale = self._ready_for_sale
        self.reg_number = self._reg_number
        self.title = self._title
        self.age_of_car = self._age_of_car
        self.usage_efficency = self._usage_efficency
        self.is_old_car = self._is_old_car
        self.is_expensive = self._is_expensive
        self.well_maintened = self._well_maintened
        self.economy_score = self._economy_score

    # le code suivant sert a s'assurer que les champs soient du bon type 
    # en gros : si brand.type = int --> ERREUR 

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def full_model_name(self):
        return self._full_model_name

    @property
    def transmission(self):
        return self._transmission

    @property
    def fuel_type(self):
        return self._fuel_type

    @property
    def make_year(self):
        return self._make_year

    @property
    def reg_year(self):
        return self._reg_year

    @property
    def engine_capacity_cc(self):
        return self._engine_capacity_cc

    @property
    def engine_category(self):
        return self._engine_category

    @property
    def km_driven(self):
        return self._km_driven

    @property
    def usage_category(self):
        return self._usage_category

    @property
    def ownership(self):
        return self._ownership

    @property
    def ownership_category(self):
        return self._ownership_category

    @property
    def price(self):
        return self._price

    @property
    def overall_cost(self):
        return self._overall_cost

    @property
    def total_value(self):
        return self._total_value

    @property
    def price_category(self):
        return self._price_category

    @property
    def has_insurance(self):
        return self._has_insurance

    @property
    def spare_key(self):
        return self._spare_key

    @property
    def ready_for_sale(self):
        return self._ready_for_sale

    @property
    def reg_number(self):
        return self._reg_number

    @property
    def title(self):
        return self._title

    @property
    def age_of_car(self):
        return self._age_of_car

    @property
    def usage_efficency(self):
        return self._usage_efficency

    @property
    def is_old_car(self):
        return self._is_old_car

    @property
    def is_expensive(self):
        return self._is_expensive

    @property
    def well_maintened(self):
        return self._well_maintened

    @property
    def economy_score(self):
        return self._economy_score
    
    @brand.setter
    def brand(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: brand must be str")
        self._brand = value

    @model.setter
    def model(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: model must be str")
        self._model = value

    @full_model_name.setter
    def full_model_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: full_model_name must be str")
        self._full_model_name = value

    @transmission.setter
    def transmission(self, value: TransmissionType):
        if not isinstance(value, TransmissionType):
            raise TypeError("[ERROR]: transmission must be TransmissionType")
        self._transmission = value

    @fuel_type.setter
    def fuel_type(self, value: FuelType):
        if not isinstance(value, FuelType):
            raise TypeError("[ERROR]: fuel_type must be FuelType")
        self._fuel_type = value

    @make_year.setter
    def make_year(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: make_year must be str")
        self._make_year = value

    @reg_year.setter
    def reg_year(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: reg_year must be str")
        self._reg_year = value

    @engine_capacity_cc.setter
    def engine_capacity_cc(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: engine_capacity_cc must be int")
        self._engine_capacity_cc = value

    @engine_category.setter
    def engine_category(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: engine_category must be str")
        self._engine_category = value

    @km_driven.setter
    def km_driven(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: km_driven must be int")
        self._km_driven = value

    @usage_category.setter
    def usage_category(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: usage_category must be str")
        self._usage_category = value

    @ownership.setter
    def ownership(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: ownership must be int")
        self._ownership = value

    @ownership_category.setter
    def ownership_category(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: ownership_category must be str")
        self._ownership_category = value

    @price.setter
    def price(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: price must be int")
        self._price = value

    @overall_cost.setter
    def overall_cost(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: overall_cost must be int")
        self._overall_cost = value

    @total_value.setter
    def total_value(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: total_value must be int")
        self._total_value = value

    @price_category.setter
    def price_category(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: price_category must be str")
        self._price_category = value

    @has_insurance.setter
    def has_insurance(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: has_insurance must be bool")
        self._has_insurance = value

    @spare_key.setter
    def spare_key(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: spare_key must be bool")
        self._spare_key = value

    @ready_for_sale.setter
    def ready_for_sale(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: ready_for_sale must be bool")
        self._ready_for_sale = value

    @reg_number.setter
    def reg_number(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: reg_number must be str")
        self._reg_number = value

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise TypeError("[ERROR]: title must be str")
        self._title = value

    @age_of_car.setter
    def age_of_car(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: age_of_car must be int")
        self._age_of_car = value

    @usage_efficency.setter
    def usage_efficency(self, value: int):
        if not isinstance(value, int):
            raise TypeError("[ERROR]: usage_efficency must be int")
        self._usage_efficency = value

    @is_old_car.setter
    def is_old_car(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: is_old_car must be bool")
        self._is_old_car = value

    @is_expensive.setter
    def is_expensive(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: is_expensive must be bool")
        self._is_expensive = value

    @well_maintened.setter
    def well_maintened(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("[ERROR]: well_maintened must be bool")
        self._well_maintened = value

    @economy_score.setter
    def economy_score(self, value: float):
        if not isinstance(value, float):
            raise TypeError("[ERROR]: economy_score must be float")
        self._economy_score = value



