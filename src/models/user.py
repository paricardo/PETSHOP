from src.models import BaseModel
from src.utils.validators import date_now
from peewee import (
    CharField,
    BooleanField
)


class User(BaseModel):
    name = CharField(max_length=50, null=False)
    email = CharField(max_length=150, null=False)
    password = CharField()
    role = CharField(default="Admin")
    is_active = BooleanField(default=True)
    created_at = date_now


    class Meta:
        table_name = "users"