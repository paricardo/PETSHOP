from flask import Flask
from src.models.init_db import initialize_database
from config import DevelopmentConfig
from src.routes.customer_route import customer_bp
from src.routes.pet_route import pet_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(pet_bp, url_prefix='/pets')

    initialize_database()

    return app