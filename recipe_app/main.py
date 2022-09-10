from pathlib import Path
from uuid import UUID, uuid4
import uvicorn
from fastapi import FastAPI, APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from recipe_app.schemas.recipe_ingredient import RecipeSchemaIn, RecipeSchemaOut, IngredientSchema
from recipe_app.models.models import Recipe


# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

load_dotenv(Path(ROOT, ".env"))

app = FastAPI(title="Recipe APIs")
api_router = APIRouter()


@api_router.on_event("startup")
def setup_tables():
    if not Recipe.exists():
        Recipe.create_table(read_capacity_units=1,
                            write_capacity_units=1, wait=True)


@api_router.get("/ping", status_code=200)
def ping() -> dict:
    return {"ping": "pong"}


@api_router.get('/recipes', status_code=200, response_model=list[RecipeSchemaOut])
def get_all_recipes(limit: int = Query(default=100, lte=100)) -> list[RecipeSchemaOut]:
    items = Recipe.scan(limit=limit)
    schemas = []

    for model in items:
        model.ingredients = [IngredientSchema(
            **ingredient.attribute_values) for ingredient in model.ingredients]
        schemas.append(RecipeSchemaOut(**model.attribute_values))

    return schemas


@api_router.get('/recipes/{recipe_id}', status_code=200, response_model=RecipeSchemaOut)
def get_recipe(recipe_id: UUID) -> RecipeSchemaOut:
    model = Recipe.get(str(recipe_id))
    model.ingredients = [IngredientSchema(
        **ingredient.attribute_values) for ingredient in model.ingredients]

    return RecipeSchemaOut(**model.attribute_values)


@api_router.post('/recipes', status_code=201, response_model=RecipeSchemaOut)
def create_recipe(recipe_in: RecipeSchemaIn) -> RecipeSchemaOut:
    dct = recipe_in.dict()
    dct["id"] = str(uuid4())
    model = Recipe(**dct)
    model.save()

    model.ingredients = [IngredientSchema(
        **ingredient) for ingredient in model.ingredients]

    return RecipeSchemaOut(**model.attribute_values)


@api_router.get('/ingredients', status_code=200, response_model=list[IngredientSchema])
def get_all_ingredients() -> list[IngredientSchema]:
    all_recipes = get_all_recipes(limit=None)
    all_ingredients = []

    for recipe in all_recipes:
        all_ingredients.extend(recipe.ingredients)

    return all_ingredients


@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """
    recipes = get_all_recipes(limit=None)
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "recipes": recipes})


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
