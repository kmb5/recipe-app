import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/recipe/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    return recipe


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
