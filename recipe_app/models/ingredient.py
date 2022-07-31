from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from recipe_app.db.base_class import Base


class Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    recipes = relationship("RecipeIngredient", back_populates="ingredients")
