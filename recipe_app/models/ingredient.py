from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    recipes: list["Recipe"] = Relationship(back_populates="ingredients")
