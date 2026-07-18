from src.models import db
from config import Config
from src.models.user import User
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.service import Service
from src.models.appointment import Appointment

def initialize_database():
    db.connect()
    db.create_tables([
        User,
        Customer,
        Pet,
        Service,
        Appointment,
    ])

    if not User.select().exists():
        User.create(
            name=Config.USER_NAME,
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD,
        )