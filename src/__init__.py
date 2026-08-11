from flask import Flask, session

from src.models.init_db import initialize_database
from config import DevelopmentConfig, ProductionConfig
from src.routes.customer_route import customer_bp
from src.routes.pet_route import pet_bp
from src.routes.package_route import package_bp
from src.routes.appointment_route import appointment_bp
from src.routes.home_route import index_bp
from src.routes.user_route import user_bp
from src.routes.auth_route import auth_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(ProductionConfig)

    @app.context_processor
    def inject_user_role():
        return {
            "user_role": session.get("user_role")
        }

    app.register_blueprint(auth_bp, url_prefix="")
    app.register_blueprint(index_bp, url_prefix="/home")
    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(pet_bp, url_prefix="/pets")
    app.register_blueprint(package_bp, url_prefix="/packages")
    app.register_blueprint(appointment_bp, url_prefix="/appointments")
    app.register_blueprint(user_bp, url_prefix="/users")

    initialize_database()

    return app