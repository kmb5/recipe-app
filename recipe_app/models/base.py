from pynamodb.models import Model
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(Path(BASE_DIR, ".env"), verbose=True)


class BaseModel(Model):
    class Meta:
        region_name = os.getenv('DB_REGION_NAME'),
        aws_access_key_id = os.getenv('DB_ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('DB_SECRET_ACCESS_KEY')
