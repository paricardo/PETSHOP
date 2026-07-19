from flask import (
    Blueprint,
    request,
    jsonify
)
from src.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

service = CustomerService()

""" ROTAS DE CRUD """

@customer_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    print(type(result))

    return jsonify(result)