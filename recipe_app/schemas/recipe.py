from typing import Sequence
from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int


class RecipeCreate(BaseModel):
    name: str
    cooking_time_min: int
    num_people: int
    kcal: int
    submitter_id: int


class RecipeUpdate(BaseModel):
    name: str


# Properties shared by models stored in DB

# Why make the distinction between a Recipe and RecipeInDB?
# This allows us in future to separate fields which are only relevant for the DB,
# or which we don’t want to return to the client (such as a password field).
class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

# Properties to return to client


class Recipe(RecipeInDBBase):
    pass


class RecipeInDB(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
