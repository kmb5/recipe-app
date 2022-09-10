import os
from pathlib import Path
import boto3
from dotenv import load_dotenv
from boto3.resources.base import ServiceResource

BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(Path(BASE_DIR, ".env"), verbose=True)

DB_URL = os.environ["DATABASE_URL"]


def initialize_db() -> ServiceResource:
    db = boto3.resource(
        'dynamodb',
        region_name=os.getenv('DB_REGION_NAME'),
        aws_access_key_id=os.getenv('DB_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('DB_SECRET_ACCESS_KEY')
    )

    return db
