from flask import Blueprint, render_template, request
from src.services.user_service import UserService
from src.services.appointment_service import AppointmentService
from src.services.customer_service import CustomerService
from src.services.package_service import PackageService

index_bp = Blueprint('home', __name__)

user_service = UserService()
appointment_service = AppointmentService()
package_service = PackageService()
customer_service = CustomerService()

@index_bp.route("/", methods=['GET'])
def index():

    appointments = appointment_service.get()
    customers = customer_service.get()
    packages = package_service.get()
    
    return render_template("home/index.html", 
                            appointments=appointments,
                            customers=customers,
                            packages=packages)