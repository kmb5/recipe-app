

class CRUDRecipe(CRUDBase[Recipe, RecipeBase, RecipeBase]):
    ...


recipe = CRUDRecipe(Recipe)
