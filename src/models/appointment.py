from src.models import BaseModel
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.package import Package
from src.models.user import User
from peewee import *


class Appointment(BaseModel):
    customer_id = ForeignKeyField(
        Customer,
        backref="appointments",
        on_delete="CASCADE"
    )

    pet_id = ForeignKeyField(
        Pet,
        backref="appointments",
        on_delete="CASCADE"
    )

    package_id = ForeignKeyField(
        Package,
        backref="appointments",
        on_delete="CASCADE"
    )


    user_id = ForeignKeyField(
        User,
        backref="appointments",
        on_delete="CASCADE"
    )

    final_price = DecimalField(null=False, max_digits=10, decimal_places=2)
    scheduled_at = DateTimeField()
    status = CharField(default="in_progress")
    notes = TextField()

    class Meta:
        table_name = "appointments"