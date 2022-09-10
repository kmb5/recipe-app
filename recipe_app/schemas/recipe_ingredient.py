from uuid import UUID
from pydantic import BaseModel


class IngredientSchema(BaseModel):
    name: str
    unit: str
    amount: int


class IngredientSchemaIn(IngredientSchema):
    pass


class IngredientSchemaOut(IngredientSchema):
    id: UUID
    #updated_at: int
    #created_at: int


class RecipeSchema(BaseModel):
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int
    ingredients: list[IngredientSchema]


class RecipeSchemaIn(RecipeSchema):
    pass


class RecipeSchemaOut(RecipeSchema):
    id: UUID
    #updated_at: int
    #created_at: int
