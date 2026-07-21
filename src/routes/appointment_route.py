from flask import Blueprint, request
from src.services.appointment_service import AppointmentService

appointment_bp = Blueprint('appointment', __name__)

service = AppointmentService()

""" ROTAS DE CRUD """

@appointment_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    data = []

    for c in result:
        value = {
            "id": c.id,
            "customer_id": c.customer_id_id,
            "pet_id": c.pet_id_id,
            "service_id": c.service_id_id,
            "user_id": c.user_id_id,
            "scheduled_at": c.scheduled_at,
            "status": c.status,
            "notes": c.notes,
            "created_at": c.created_at,
        }
        data.append(value)

    return data


@appointment_bp.route('/<int:id_appointment>', methods=['GET'])
def list_one(id_appointment: int):
    
    try:
        result = service.getById(id_appointment)

        data = [
            {
                "id": result.id,
                "customer_id": result.customer_id_id,
                "pet_id": result.pet_id_id,
                "service_id": result.service_id_id,
                "user_id": result.user_id_id,
                "scheduled_at": result.scheduled_at,
                "status": result.status,
                "notes": result.notes,
                "created_at": result.created_at,
            }
        ]

        return data
    except Exception:
        return result

    
@appointment_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@appointment_bp.route('/update/<int:id_appointment>', methods=['POST'])
def update(id_appointment):
    data = request.form.to_dict()

    result = service.update(data, id_appointment)

    return result


@appointment_bp.route('/delete/<int:id_appointment>', methods=['POST'])
def delete(id_appointment):

    result = service.delete(id_appointment)

    return result