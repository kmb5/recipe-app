from typing import Generator
from sqlmodel import Session
from recipe_app.db.session import engine


def get_session() -> Generator:
    with Session(engine) as session:
        yield session
