from flask import Blueprint, request
from src.services.pet_service import PetService

pet_bp = Blueprint('pets', __name__)

service = PetService()

@pet_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    data = []

    for c in result:
        value = {
            "id": c.id, 
            "name": c.name, 
            "breed": c.breed, 
            "notes": c.notes, 
            "is_active": c.is_active, 
            "created_at": c.created_at, 
            "customer_id": c.customer_id_id,
        }
        data.append(value)

    return data


@pet_bp.route('/<int:id_pet>', methods=['GET'])
def list_one(id_pet):
    try:
        result = service.getById(id_pet)

        data = [
            {
                "id": result.id, 
                "name": result.name, 
                "breed": result.breed, 
                "notes": result.notes, 
                "is_active": result.is_active, 
                "created_at": result.created_at, 
                "customer_id": result.customer_id_id,
            }
        ]

        return data
    except Exception:
        
        return result


@pet_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@pet_bp.route('/update/<int:id_pet>', methods=['POST'])
def update(id_pet):
    ...


@pet_bp.route('/delete/<int:id_pet>', methods=['POST'])
def delete(id_pet):
    ...