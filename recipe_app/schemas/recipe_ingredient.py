from __future__ import annotations

from typing import Sequence, Any
from unittest.util import strclass
from pydantic import BaseModel

from recipe_app.schemas.user import User


class RecipeBase(BaseModel):
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int
    submitter_id: int
    ingredients: list[Any]


class RecipeCreate(RecipeBase):
    pass


class RecipeInDBBase(BaseModel):
    id: int
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int
    submitter_id: int
    submitter: User
    ingredients: list[Any]

    class Config:
        orm_mode = True


class Ingredient(BaseModel):
    name: str

    class Config:
        orm_mode = True


class IngredientBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredient_id: int
    amount: int
    unit: str
    ingredient: Ingredient

    class Config:
        orm_mode = True


class RecipeSearchResults(BaseModel):
    results: Sequence[Any]


RecipeInDBBase.update_forward_refs()
