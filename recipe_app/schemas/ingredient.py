from recipe_app.schemas.recipe import RecipeBase
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    recipes: list[RecipeBase]
