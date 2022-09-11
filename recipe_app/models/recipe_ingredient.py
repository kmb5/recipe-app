from uuid import uuid4
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, ListAttribute, MapAttribute

from recipe_app.models.base import BaseModel


class Ingredient(MapAttribute):

    name = UnicodeAttribute(null=False)
    search_name = UnicodeAttribute(null=True)
    amount = NumberAttribute(null=False)
    unit = UnicodeAttribute(null=False)


class Recipe(BaseModel):

    class Meta(BaseModel.Meta):
        table_name = "recipes"

    id = UnicodeAttribute(hash_key=True, default=uuid4)
    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=True)
    search_name = UnicodeAttribute(null=False)
    cooking_time_min = NumberAttribute(null=False)
    num_people = NumberAttribute(null=False)
    kcal = NumberAttribute(null=False)
    ingredients = ListAttribute(of=Ingredient)
    steps = ListAttribute(of=UnicodeAttribute)
