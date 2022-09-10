import os
from pathlib import Path
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, ListAttribute
from pynamodb.models import Model
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(Path(BASE_DIR, ".env"), verbose=True)


class BaseModel(Model):
    class Meta:
        region = os.getenv('DB_REGION_NAME'),
        aws_access_key_id = os.getenv('DB_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('DB_SECRET_ACCESS_KEY')


# class User(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, index=True)
#     username: str
#     email: str = Field(default=None)
#     is_superuser: bool = Field(default=False)
#     recipes: list["Recipe"] = Relationship(back_populates="submitter")


class Ingredient(BaseModel):
    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    unit = UnicodeAttribute(null=False)
    amount = NumberAttribute(null=False)


class Recipe(BaseModel):
    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    cooking_time_min = NumberAttribute(null=False)
    num_people = NumberAttribute(null=False)
    kcal = NumberAttribute(null=False)
    ingredients = ListAttribute(of=Ingredient)
