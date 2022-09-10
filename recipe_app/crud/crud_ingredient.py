
class CRUDIngredient(CRUDBase[Ingredient, IngredientBase, IngredientBase]):
    ...


ingredient = CRUDIngredient(Ingredient)
