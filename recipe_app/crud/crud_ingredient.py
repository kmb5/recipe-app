from recipe_app.crud.base import CRUDBase
from recipe_app.models.ingredient import Ingredient
from recipe_app.schemas.recipe_ingredient import IngredientBase


class CRUDIngredient(CRUDBase[Ingredient, IngredientBase, IngredientBase]):
    ...


ingredient = CRUDIngredient(Ingredient)
