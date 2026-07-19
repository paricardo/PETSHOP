from flask import Flask
from src.routes.customer_route import customer_bp
from src.models.init_db import initialize_database
from config import DevelopmentConfig

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(customer_bp, url_prefix="/customers")

    initialize_database()

    return app