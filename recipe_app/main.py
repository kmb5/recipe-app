from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from recipe_app import crud
from recipe_app import deps
from recipe_app.schemas.recipe import Recipe, RecipeCreate

# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

load_dotenv(Path(ROOT, ".env"))

app = FastAPI(title="Recipe API")
api_router = APIRouter()


@api_router.get("/ping", status_code=200)
def ping() -> dict:
    return {"ping": "pong"}


@api_router.get("/", status_code=200)
def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
    """
    Root GET
    """
    recipes = crud.recipe.get_multi(db=db, limit=10)
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "recipes": recipes})


@api_router.get('/recipe/{recipe_id}', status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = crud.recipe.get(db=db, id=recipe_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Recipe with id {recipe_id} not found")
    return result


@api_router.post('/recipe/', status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate, db: Session = Depends(deps.get_db)) -> dict:
    """
    Create a new recipe in the database
    """

    recipe = crud.recipe.create(db=db, obj_in=recipe_in)

    return recipe

    # @app.post("/recipe/", response_model=RecipeBase)
    # def create_recipe(recipe: Recipe):
    #     recipe = CRUDRecipe(Recipe).create()
    #     db_recipe = Recipe(
    #         name=recipe.name, cooking_time_min=recipe.cooking_time_min, num_people=recipe.num_people, kcal=recipe.kcal
    #     )
    #     db.session.add(db_recipe)
    #     db.session.commit()
    #     return db_recipe
    # @app.get("/recipes/", response_model=list[SchemaRecipe])
    # def get_recipes():
    #     return db.session.query(ModelRecipe).all()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
