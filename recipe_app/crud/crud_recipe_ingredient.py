from recipe_app.crud.base import CRUDBase
from recipe_app.models.recipe import Recipe
from recipe_app.schemas.recipe_ingredient import RecipeIngredientBase


class CRUDRecipeIngredient(CRUDBase[Recipe, RecipeIngredientBase, RecipeIngredientBase]):
    ...


recipe_ingredient = CRUDRecipeIngredient(Recipe)
