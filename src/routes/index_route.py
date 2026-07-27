from flask import Blueprint, render_template, request
from src.services.customer_service import CustomerService
from src.services.package_service import PackageService

customerService = CustomerService()
packageService = PackageService()

index_bp = Blueprint('index', __name__)


@index_bp.route("/", methods=['GET'])
def index():
    customers = customerService.get()

    packages = packageService.get()

    message = request.args.get("message")

    return render_template("index/index.html", 
                                customers=customers,
                                message=message,
                                packages=packages,
                           )