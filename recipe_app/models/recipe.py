from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from recipe_app.db.base_class import Base


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cooking_time_min = Column(Integer)
    num_people = Column(Integer)
    kcal = Column(Integer)
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="recipes")
