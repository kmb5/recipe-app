from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str
    email: str = Field(default=None)
    is_superuser: bool = Field(default=False)
    recipes: list["Recipe"] = Relationship(back_populates="submitter")
