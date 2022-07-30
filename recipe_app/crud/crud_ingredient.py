from recipe_app.crud.base import CRUDBase
from recipe_app.models.ingredient import Ingredient
from recipe_app.schemas.ingredient import IngredientCreate, IngredientUpdate


class CRUDIngredient(CRUDBase[Ingredient, IngredientCreate, IngredientUpdate]):
    ...


ingredient = CRUDIngredient(Ingredient)
