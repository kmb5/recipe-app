from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    cooking_time_min: int
    num_people: int
    kcal: int
    submitter_id: Optional[int] = Field(default=None, foreign_key="user.id")
    submitter: Optional["User"] = Relationship(back_populates="recipes")
    ingredients: Optional["RecipeIngredient"] = Relationship(
        back_populates="recipes")
