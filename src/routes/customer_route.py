from flask import Blueprint, request
from src.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

service = CustomerService()

""" ROTAS DE CRUD """

@customer_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    data = []

    for c in result:
        value = {
            "id": c.id, 
            "name": c.name, 
            "phone": c.phone, 
            "email": c.email, 
            "address": c.address, 
            "notes": c.notes, 
            "is_active": c.is_active, 
            "created_at": c.created_at,
        }
        data.append(value)

    return data


@customer_bp.route('/<int:id_customer>', methods=['GET'])
def list_one(id_customer: int):
    
    try:
        result = service.getById(id_customer)

        data = [
            {
                "id": result.id, 
                "nome": result.name, 
                "phone": result.phone, 
                "email": result.email, 
                "address": result.address, 
                "notes": result.notes, 
                "is_active": result.is_active
            }
        ]

        return data
    except Exception:
        
        return result

    
@customer_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@customer_bp.route('/update/<int:id_customer>', methods=['POST'])
def update(id_customer):
    data = request.form.to_dict()

    result = service.update(data, id_customer)

    return result


@customer_bp.route('/delete/<int:id_customer>', methods=['POST'])
def delete(id_customer):

    result = service.delete(id_customer)

    return result