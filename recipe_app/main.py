import re
from pathlib import Path
from uuid import UUID, uuid4
import json
import uvicorn
from fastapi import FastAPI, APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from recipe_app.schemas.recipe_ingredient import RecipeSchemaIn, RecipeSchemaOut, IngredientSchema, RecipeSearch
from recipe_app.schemas.pantry import PantryItemSchemaIn, PantryItemSchemaOut
from recipe_app.models.recipe_ingredient import Recipe
from recipe_app.models.pantry import PantryItem
from recipe_app.base_recipes import recipes


# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

load_dotenv(Path(ROOT, ".env"))

app = FastAPI(title="Recipes API")
api_router = APIRouter()


@api_router.on_event("startup")
def setup_tables():
    if not Recipe.exists():
        Recipe.create_table(read_capacity_units=1,
                            write_capacity_units=1, wait=True)

    cnt = len(list(Recipe.scan()))
    if cnt == 0:
        print('Setting up base recipes...')
        with Recipe.batch_write() as batch:
            base_recipes = _prepare_base_recipes()
            for item in base_recipes:
                batch.save(item)

    if not PantryItem.exists():
        PantryItem.create_table(read_capacity_units=1,
                                write_capacity_units=1, wait=True)


def _prepare_base_recipes():
    base_recipes = [Recipe(**recipe) for recipe in recipes]
    for r in base_recipes:
        r.id = str(uuid4())

    return base_recipes


@api_router.get("/ping", status_code=200)
def ping() -> dict:
    return {"ping": "pong"}


@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """
    recipes = get_all_recipes(limit=None)
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "recipes": recipes})


@api_router.get('/recipes', status_code=200, response_model=list[RecipeSchemaOut])
def get_all_recipes(limit: int = Query(default=100, lte=100)) -> list[RecipeSchemaOut]:
    items = Recipe.scan(limit=limit)
    schemas = []

    for model in items:
        m = json.loads(model.to_json())
        schemas.append(RecipeSchemaOut(**m))
    return schemas


@api_router.get('/recipes/{recipe_id}', status_code=200, response_model=RecipeSchemaOut)
def get_recipe(recipe_id: UUID) -> RecipeSchemaOut:
    model = Recipe.get(str(recipe_id))
    model = json.loads(model.to_json())
    return RecipeSchemaOut(**model)


@api_router.post('/recipes', status_code=201, response_model=RecipeSchemaOut)
def create_recipe(recipe_in: RecipeSchemaIn) -> RecipeSchemaOut:
    dct = recipe_in.dict()
    dct["id"] = str(uuid4())
    dct["search_name"] = _create_search_name(recipe_in.name)
    model = Recipe(**dct)
    model.save()

    model = json.loads(model.to_json())
    return RecipeSchemaOut(**model)


def _create_search_name(name: str) -> str:
    name_lower = name.lower()
    return re.sub(r'[^a-z\ ]', '', name_lower).strip()


@api_router.post('/recipes/search', status_code=200, response_model=list[RecipeSchemaOut] | None)
def search_recipes(recipe_search: RecipeSearch) -> list[RecipeSchemaOut]:
    schemas = []
    if recipe_search.name:
        found = [item for item in Recipe.scan(
            Recipe.search_name.contains(recipe_search.name.lower()))]
        if found:
            for item in found:
                model = json.loads(item.to_json())
                schemas.append(RecipeSchemaOut(**model))

    if recipe_search.ingredients:
        pass

    return schemas


@api_router.get('/ingredients', status_code=200, response_model=list[IngredientSchema])
def get_all_ingredients() -> list[IngredientSchema]:
    all_recipes = get_all_recipes(limit=None)
    all_ingredients = []

    for recipe in all_recipes:
        all_ingredients.extend(recipe.ingredients)

    return all_ingredients


@api_router.post('/pantry', status_code=201, response_model=PantryItemSchemaOut)
def create_pantry_item(pantry_item: PantryItemSchemaIn) -> PantryItemSchemaOut:
    dct = pantry_item.dict()
    dct["id"] = str(uuid4())
    model = PantryItem(**dct)
    model.save()

    model = json.loads(model.to_json())
    return PantryItemSchemaOut(**model)


@api_router.get('/pantry/{pantry_item_id}', status_code=200, response_model=PantryItemSchemaOut)
def get_pantry_item(pantry_item_id: UUID) -> PantryItemSchemaOut:
    model = PantryItem.get(str(pantry_item_id))
    model = json.loads(model.to_json())
    return PantryItemSchemaOut(**model)


@api_router.get('/pantry', status_code=200, response_model=list[PantryItemSchemaOut])
def get_all_pantry_items(limit: int = Query(default=100, lte=100)) -> list[PantryItemSchemaOut]:
    items = PantryItem.scan(limit=limit)
    schemas = []

    for model in items:
        m = json.loads(model.to_json())
        schemas.append(PantryItemSchemaOut(**m))
    return schemas


@api_router.get('/pantry/search/{pantry_item_name}', status_code=200, response_model=list[PantryItemSchemaOut])
def search_pantry_items(pantry_item_name: str) -> list[PantryItemSchemaOut]:
    schemas = []
    for item in PantryItem.name_index.query(pantry_item_name):
        model = json.loads(item.to_json())
        schemas.append(PantryItemSchemaOut(**model))

    return schemas


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
