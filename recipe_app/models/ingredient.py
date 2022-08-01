from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class IngredientBase(SQLModel):
    name: str = Field(index=True)


class Ingredient(IngredientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    recipes: list["RecipeIngredient"] = Relationship(
        back_populates="ingredients")


class IngredientCreate(IngredientBase):
    pass


class IngredientRead(IngredientBase):
    id: int


class IngredientUpdate(SQLModel):
    name: Optional[str] = None
    #recipes: Optional[list["Recipe"]] = None
