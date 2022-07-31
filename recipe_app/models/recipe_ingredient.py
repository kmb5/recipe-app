from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class RecipeIngredient(SQLModel, table=True):
    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipe.id", primary_key=True)
    ingredient_id: Optional[int] = Field(
        default=None, foreign_key="ingredient.id", primary_key=True)
    amount: int
    unit: str
    recipes: list["Recipe"] = Relationship(back_populates="ingredients")
    ingredients: list["Ingredient"] = Relationship(back_populates="recipes")
