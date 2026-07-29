from peewee import Model, AutoField, DateTimeField, SqliteDatabase
from src.utils.validators import now_without_seconds
from config import Config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

db = SqliteDatabase(BASE_DIR / Config.DATABASE)

class BaseModel(Model):
    id = AutoField()
    created_at = DateTimeField(default=now_without_seconds)

    class Meta:
        database = db