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

    data = []

    for c in result:
        value = {"id": c.id, "nome": c.name, "phone": c.phone, "email": c.email, "address": c.address, "notes": c.notes, "is_active": c.is_active}
        data.append(value)

    return data

@customer_bp.route('/<int:id_customer>', methods=['GET'])
def list_one(id_customer: int):
    
    try:
        result = service.getById(id_customer)

        data = [{"id": result.id, "nome": result.name, "phone": result.phone, "email": result.email, "address": result.address, "notes": result.notes, "is_active": result.is_active}]

        return data
    except Exception:
        
        return result

    