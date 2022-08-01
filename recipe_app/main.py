from pathlib import Path
from typing import Any, Optional

import uvicorn
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates

from sqlmodel import Session, select
from dotenv import load_dotenv

from recipe_app import deps
from recipe_app.models import *


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
def root(request: Request, db_session: Session = Depends(deps.get_session)) -> dict:
    """
    Root GET
    """
    recipes = db_session.exec(select(Recipe).offset(0).limit(100)).all()
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "recipes": recipes})


@api_router.get('/ingredients/{ingredient_id}', status_code=200, response_model=IngredientReadWithRecipe)
def read_ingredient(ingredient_id: int, db_session: Session = Depends(deps.get_session)):
    """
    Read a single ingredient by ID
    """
    result = db_session.get(Ingredient, ingredient_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Ingredient with id {ingredient_id} not found")
    return result


@api_router.get('/ingredients/', status_code=200, response_model=list[IngredientReadWithRecipe])
def get_all_ingredients(offset: int = 0, limit: int = Query(default=100, lte=100), db_session: Session = Depends(deps.get_session)):

    return db_session.exec(select(Ingredient).offset(offset).limit(limit)).all()


@api_router.get('/recipes/', status_code=200, response_model=list[RecipeReadWithIngredients])
def get_all_recipes(offset: int = 0, limit: int = Query(default=100, lte=100), db_session: Session = Depends(deps.get_session)):
    return db_session.exec(select(Recipe).offset(offset).limit(limit)).all()


@api_router.get('/recipes/{recipe_id}', status_code=200, response_model=RecipeReadWithIngredients)
def read_recipe(recipe_id: int, db_session: Session = Depends(deps.get_session)):
    """
    Read a single ingredient by ID
    """
    result = db_session.get(Recipe, recipe_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Ingredient with id {recipe_id} not found")
    return result


@api_router.post('/ingredients/', status_code=201, response_model=IngredientReadWithRecipe)
def create_ingredient(ingredient_in: IngredientCreate, db_session: Session = Depends(deps.get_session)):
    """Create a new ingredient in the database"""

    db_ingredient = Ingredient.from_orm(ingredient_in)
    db_session.add(db_ingredient)
    db_session.commit()
    db_session.refresh(db_ingredient)
    return db_ingredient


@api_router.patch("/ingredients/{ingredient_id}", response_model=IngredientRead)
def update_ingredient(ingredient_id: int, ingredient: IngredientUpdate, db_session: Session = Depends(deps.get_session)):
    db_ingredient = db_session.get(Ingredient, ingredient_id)
    if not db_ingredient:
        raise HTTPException(status_code=404, detaul="Ingredient not found")
    ingredient_data = ingredient.dict(exclude_unset=True)
    for k, v in ingredient_data.items():
        setattr(db_ingredient, k, v)
    db_session.add(db_ingredient)
    db_session.commit()
    db_session.refresh(db_ingredient)
    return db_ingredient


@api_router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db_session: Session = Depends(deps.get_session)):
    ingredient = db_session.get(Ingredient, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db_session.delete(ingredient)
    db_session.commit()
    return {"ok": True}


@api_router.post('/recipes/', status_code=201, response_model=RecipeReadWithIngredients)
def create_recipe(recipe_in: RecipeCreate, db_session: Session = Depends(deps.get_session)):
    """Create a new ingredient in the database"""

    db_recipe = Recipe.from_orm(recipe_in)
    db_session.add(db_recipe)
    db_session.commit()
    db_session.refresh(db_recipe)
    return db_recipe

# --------

# @api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
# def search_recipes(
#     *,
#     keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
#     max_results: Optional[int] = 10,
#     db_session: Session = Depends(deps.get_session)
# ) -> dict:
#     recipes = crud.recipe.get_multi(db=db_session, limit=max_results)
#     if not keyword:
#         return {"results": recipes}

#     results = filter(lambda recipe: keyword.lower()
#                      in recipe.name.lower(), recipes)
#     return {"results": list(results)[:max_results]}


# @api_router.post('/recipe/', status_code=201, response_model=RecipeInDBBase)
# def create_recipe(*, recipe_in: RecipeBase, db_session: Session = Depends(deps.get_session)) -> dict:
#     """
#     Create a new recipe in the database
#     """

#     print(recipe_in)


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
