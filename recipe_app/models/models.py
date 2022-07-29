from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cooking_time_min = Column(Integer)
    num_people = Column(Integer)
    kcal = Column(Integer)
