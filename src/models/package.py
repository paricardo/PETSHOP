from src.models import BaseModel
from peewee import CharField ,TextField, DecimalField, IntegerField


class Package(BaseModel):
    name = CharField(null=False)
    services = TextField()
    quantity = IntegerField(null=False, default=1)

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


    class Meta:
        table_name = "packages"