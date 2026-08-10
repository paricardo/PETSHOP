from src.models import db
from config import Config
from src.models.user import User
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.package import Package
from src.models.appointment import Appointment
from werkzeug.security import generate_password_hash

def initialize_database():
    db.connect()
    db.create_tables([
        User,
        Customer,
        Pet,
        Package,
        Appointment,
    ])

    if not User.select().exists():
        User.create(
            name=Config.USER_NAME,
            email=Config.USER_EMAIL,
            password=generate_password_hash(Config.USER_PASSWORD)
        )