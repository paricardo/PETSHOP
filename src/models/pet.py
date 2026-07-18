from src.models import BaseModel
from src.models.customer import Customer
from src.utils.validators import date_now
from peewee import (
    CharField,
    TextField,
    BooleanField,
    ForeignKeyField
)


class Pet(BaseModel):
    name = CharField(max_length=50, null=False)
    breed = CharField(max_length=50)
    notes = TextField(null=True)
    is_active = BooleanField(default=True)
    created_at = date_now

    customer_id = ForeignKeyField(
        Customer,
        backref="pets",
        on_delete="CASCADE"
    )

    class Meta:
        table_name = "pets"