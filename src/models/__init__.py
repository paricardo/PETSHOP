from peewee import Model, AutoField, DateTimeField, SqliteDatabase
from src.utils.validators import validate_hours
from config import Config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

db = SqliteDatabase(BASE_DIR / Config.DATABASE)

class BaseModel(Model):
    id = AutoField()
    created_at = validate_hours()

    class Meta:
        database = db