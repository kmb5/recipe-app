from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class RecipeBase(SQLModel):
    name: str = Field(index=True)
    cooking_time_min: int
    num_people: int
    kcal: int


class Recipe(RecipeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    submitter_id: Optional[int] = Field(default=None, foreign_key="user.id")
    submitter: Optional["User"] = Relationship(back_populates="recipes")
    ingredients: list["Ingredient"] = Relationship(back_populates="recipe")


class RecipeCreate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    id: int


class RecipeUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    cooking_time_min: Optional[int] = None
    num_people: Optional[int] = None
    kcal: Optional[int] = None


class IngredientBase(SQLModel):
    name: str = Field(index=True)
    quantity: str
    amount: int
    recipe_id: Optional[int] = Field(default=None, foreign_key="recipe.id")


class Ingredient(IngredientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    recipe: Optional[Recipe] = Relationship(back_populates="ingredients")


class IngredientRead(IngredientBase):
    id: int


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(SQLModel):
    name: Optional[str] = None
    quantity: Optional[str] = None
    amount: Optional[int] = None


class RecipeReadWithIngredients(RecipeRead):
    ingredients: list[Ingredient] = []


class IngredientReadWithRecipe(IngredientRead):
    recipe: Optional[Recipe] = None
