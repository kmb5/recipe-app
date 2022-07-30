from recipe_app.schemas.ingredient import IngredientBase
from recipe_app.schemas.recipe import RecipeBase

from pydantic import BaseModel


class RecipeIngredientBase(BaseModel):
    amount: int
    unit: str
    recipes: list[RecipeBase]
    ingredients: list[IngredientBase]
