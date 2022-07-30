from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from recipe_app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=True)
    email = Column(String(256), nullable=True)
    is_superuser = Column(Boolean, default=False)
    recipes = relationship(
        "Recipe",
        cascade="all, delete-orphan",
        back_populates="submitter",
        uselist=True
    )
