import os
from pathlib import Path
from uuid import uuid4
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, ListAttribute, MapAttribute
from pynamodb.models import Model
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(Path(BASE_DIR, ".env"), verbose=True)


class BaseModel(Model):
    class Meta:
        region_name = os.getenv('DB_REGION_NAME'),
        aws_access_key_id = os.getenv('DB_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('DB_SECRET_ACCESS_KEY')


class Ingredient(MapAttribute):

    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=True)
    amount = NumberAttribute(null=False)
    unit = UnicodeAttribute(null=False)


class Recipe(BaseModel):

    class Meta(BaseModel.Meta):
        table_name = "recipes"

    id = UnicodeAttribute(hash_key=True, default=uuid4)
    name = UnicodeAttribute(null=False)
    cooking_time_min = NumberAttribute(null=False)
    num_people = NumberAttribute(null=False)
    kcal = NumberAttribute(null=False)
    ingredients = ListAttribute(of=Ingredient)
    steps = ListAttribute(of=UnicodeAttribute)
