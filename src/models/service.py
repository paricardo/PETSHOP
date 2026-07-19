from src.models import BaseModel
from src.utils.validators import date_now
from peewee import (
    CharField,
    TextField,
    DecimalField,
)


class Service(BaseModel):
    name = CharField(max_length=150, null=False)
    notes = TextField()

    price_small = DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0, 
        null=False, 
        auto_round=False)
    
    price_medium = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        auto_round=False
    )

    price_large = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        auto_round=False
    )

    created_at = date_now

    class Meta:
        table_name = "services"