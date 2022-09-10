
class CRUDRecipeIngredient(CRUDBase[Recipe, RecipeIngredientBase, RecipeIngredientBase]):
    ...


recipe_ingredient = CRUDRecipeIngredient(Recipe)
