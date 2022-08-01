import os
from pathlib import Path
from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(Path(BASE_DIR, ".env"), verbose=True)

DB_URL = os.environ["DATABASE_URL"]

engine = create_engine(DB_URL)
