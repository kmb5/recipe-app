import time
import uuid
from typing import Dict, Any, Union

from recipe_app.schemas.recipe_ingredient import RecipeSchemaIn, RecipeSchemaOut, IngredientSchemaIn, IngredientSchemaOut
from recipe_app.models.models import Recipe, Ingredient


class RecipeRepository:
    table: Recipe = Recipe
    schema_out: RecipeSchemaOut = RecipeSchemaOut

    @staticmethod
    def _preprocess_create(values: Dict[str, Any]) -> Dict[str, Any]:
        #imestamp_now = time.time()
        values["id"] = str(uuid.uuid4())
        #values["created_at"] = timestamp_now
        #values["updated_at"] = timestamp_now

        return values

    @classmethod
    def create(cls, recipe_in: RecipeSchemaIn) -> RecipeSchemaOut:
        data = cls._preprocess_create(recipe_in.dict())
        model: Recipe = cls.table(**data)
        model.save()
        return cls.schema_out(**model.attribute_values)

    @classmethod
    def get(cls, entry_id: Union[str, uuid.UUID]) -> RecipeSchemaOut:
        model = cls.table.get(str(entry_id))
        return cls.schema_out(**model.attribute_values)

    @classmethod
    def get_all(cls) -> list[RecipeSchemaOut]:
        items = cls.table.scan()
        print(items.next())
        return [cls.schema_out(**model.attribute_values) for model in items]


class IngredientRepository:
    table: Ingredient = Ingredient
    schema_out: IngredientSchemaOut = IngredientSchemaOut

    @staticmethod
    def _preprocess_create(values: Dict[str, Any]) -> Dict[str, Any]:
        #timestamp_now = time.time()
        values["id"] = str(uuid.uuid4())
        #values["created_at"] = timestamp_now
        #values["updated_at"] = timestamp_now

        return values

    @classmethod
    def create(cls, ingredient_in: IngredientSchemaIn) -> IngredientSchemaOut:
        data = cls._preprocess_create(ingredient_in.dict())
        model: Recipe = cls.table(**data)
        model.save()
        return cls.schema_out(**model.attribute_values)

    @classmethod
    def get(cls, entry_id: Union[str, uuid.UUID]) -> IngredientSchemaOut:
        model = cls.table.get(str(entry_id))
        return cls.schema_out(**model.attribute_values)
