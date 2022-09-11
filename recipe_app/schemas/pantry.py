from datetime import datetime
from uuid import UUID
from recipe_app.schemas.recipe_ingredient import Unit
from enum import Enum
from pydantic import BaseModel


class Packaging(str, Enum):
    # subclassing from str will avoid jsonDecode errors
    GLASS = 'glass'
    CAN = 'can'
    PACKAGE = 'package'
    CARTON = 'carton'


class PantryItemSchema(BaseModel):
    name: str
    brand: str
    description: str
    amount: int
    unit: Unit
    packaging: Packaging
    expiry: datetime


class PantryItemSchemaIn(PantryItemSchema):
    pass


class PantryItemSchemaOut(PantryItemSchema):
    id: UUID
