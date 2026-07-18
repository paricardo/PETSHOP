from src.utils.validators import date_now
from src.models import BaseModel
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.service import Service
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

    service_id = ForeignKeyField(
        Service,
        backref="appointments",
        on_delete="CASCADE"
    )


    user_id = ForeignKeyField(
        User,
        backref="appointments",
        on_delete="CASCADE"
    )

    scheduled_at = DateTimeField()
    status = CharField(default="in_progress")
    notes = TextField()
    created_at = date_now

    class Meta:
        table_name = "appointments"