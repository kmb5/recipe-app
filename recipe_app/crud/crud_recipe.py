from recipe_app.crud.base import CRUDBase
from recipe_app.models.recipe import Recipe
from recipe_app.schemas.recipe import RecipeCreate, RecipeUpdate


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    ...


recipe = CRUDRecipe(Recipe)
