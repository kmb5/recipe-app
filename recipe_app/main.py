from pathlib import Path
import os

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from .models.models import Recipe as ModelRecipe
from .schema import Recipe as SchemaRecipe

BASE_DIR = Path(__file__).parent.parent
load_dotenv(Path(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/recipe/", response_model=SchemaRecipe)
def create_recipe(recipe: SchemaRecipe):
    db_recipe = ModelRecipe(
        name=recipe.name, cooking_time_min=recipe.cooking_time_min, num_people=recipe.num_people, kcal=recipe.kcal
    )
    db.session.add(db_recipe)
    db.session.commit()
    return db_recipe


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
