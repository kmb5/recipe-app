from lib2to3.pytree import Base
from uuid import uuid4
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute

from recipe_app.models.base import BaseModel
from recipe_app.models.index import PantryNameIndex


class PantryItem(BaseModel):
    class Meta(BaseModel.Meta):
        table_name = "pantry"

    id = UnicodeAttribute(hash_key=True, default=uuid4)
    name_index = PantryNameIndex()
    name = UnicodeAttribute(null=False)
    brand = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=False)
    amount = NumberAttribute(null=False)
    unit = UnicodeAttribute(null=False)
    packaging = UnicodeAttribute(null=False)
    expiry = UTCDateTimeAttribute(null=False)
