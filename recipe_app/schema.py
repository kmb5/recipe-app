from lib2to3.pytree import Base
from pydantic import BaseModel


class Recipe(BaseModel):
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int

    class Config:
        orm_mode = True
