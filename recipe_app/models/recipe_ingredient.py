from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from recipe_app.db.base_class import Base


class RecipeIngredient(Base):
    recipe_id = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey(
        "ingredient.id"), primary_key=True)
    amount = Column(Integer)
    unit = Column(String)
    recipes = relationship("Recipe", back_populates="ingredients")
    ingredients = relationship("Ingredient", back_populates="recipes")
