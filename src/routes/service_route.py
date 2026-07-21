from flask import Blueprint, request
from src.services.service_service import ServiceService

service_bp = Blueprint('service', __name__)

service = ServiceService()

""" ROTAS DE CRUD """

@service_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    data = []

    for c in result:
        value = {
            "id": c.id,
            "name": c.name,
            "notes": c.notes,
            "price_small": c.price_small,
            "price_medium": c.price_medium,
            "price_large": c.price_large,
            "created_at": c.created_at,
        }
        data.append(value)

    return data


@service_bp.route('/<int:id_service>', methods=['GET'])
def list_one(id_service: int):
    
    try:
        result = service.getById(id_service)

        data = [
            {
                "id": result.id,
                "name": result.name,
                "notes": result.notes,
                "price_small": result.price_small,
                "price_medium": result.price_medium,
                "price_large": result.price_large,
                "created_at": result.created_at,
            }
        ]

        return data
    except Exception:
        return result

    
@service_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@service_bp.route('/update/<int:id_service>', methods=['POST'])
def update(id_service):
    data = request.form.to_dict()

    result = service.update(data, id_service)

    return result


@service_bp.route('/delete/<int:id_service>', methods=['POST'])
def delete(id_service):

    result = service.delete(id_service)

    return result