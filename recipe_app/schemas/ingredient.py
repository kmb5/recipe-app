from recipe_app.schemas.recipe import RecipeBase
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    recipes: list[RecipeBase]


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(IngredientBase):
    pass


class IngredientInDBBase(IngredientBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

# Properties to return to client


class Ingredient(IngredientInDBBase):
    pass


class IngredientInDB(IngredientInDBBase):
    pass
