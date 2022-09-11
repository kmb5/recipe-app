from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute


class PantryNameIndex(GlobalSecondaryIndex):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    name = UnicodeAttribute(default='', hash_key=True)
