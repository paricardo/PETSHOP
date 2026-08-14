from peewee import Model, AutoField, DateTimeField, SqliteDatabase
from playhouse.db_url import connect
from datetime import datetime
from zoneinfo import ZoneInfo
from config import Config
from pathlib import Path

db = connect(Config.DATABASE_URL)

def agora_sp():
    return datetime.now(ZoneInfo("America/Sao_Paulo"))

class TimestampTZField(DateTimeField):
    field_type = 'TIMESTAMPTZ'

class BaseModel(Model):
    id = AutoField()
    created_at = TimestampTZField(default=agora_sp)

    class Meta:
        database = db