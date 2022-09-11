from typing import List
from enum import Enum
from uuid import UUID
from pydantic import BaseModel


class Unit(Enum):
    GRAM = 'g'
    LITER = 'l'
    MILLILITER = 'ml'
    PIECE = 'piece'


class IngredientSchema(BaseModel):
    name: str
    amount: int
    unit: Unit


class RecipeSchema(BaseModel):
    name: str
    description: str | None
    cooking_time_min: int
    num_people: int
    kcal: int
    ingredients: List[IngredientSchema]
    steps: List[str]


class RecipeSchemaIn(RecipeSchema):
    pass


class RecipeSchemaOut(RecipeSchema):
    id: UUID
