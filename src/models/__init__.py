from peewee import SqliteDatabase, Model, AutoField
from config import Config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

db = SqliteDatabase(BASE_DIR / Config.DATABASE)

class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db