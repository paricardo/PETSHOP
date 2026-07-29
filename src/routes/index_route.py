from flask import Blueprint, render_template, request
from src.services.customer_service import CustomerService
from src.services.package_service import PackageService
from src.services.user_service import UserService

customerService = CustomerService()
packageService = PackageService()
userService = UserService()

index_bp = Blueprint('index', __name__)


@index_bp.route("/", methods=['GET'])
def index():
    customers = customerService.get()

    packages = packageService.get()

    users = userService.get()

    message = request.args.get("message")

    return render_template("index/index.html", 
                                customers=customers,
                                message=message,
                                packages=packages,
                                users=users
                           )