from src.models import BaseModel
from peewee import (
    CharField,
    TextField,
    BooleanField
)

class Customer(BaseModel):
    name = CharField(max_length=150)
    phone = CharField(max_length=20 ,unique=True, null=False)
    email = CharField(max_length=150 ,unique=True, null=True)
    address = TextField(null=False)
    sector = CharField(null=True)
    notes = TextField(null=True)
    is_active = BooleanField(default=True)


    class Meta:
        table_name = "customers"