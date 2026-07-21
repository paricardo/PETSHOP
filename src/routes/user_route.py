from flask import Blueprint, request
from src.services.user_service import UserService

user_bp = Blueprint('pets', __name__)

service = UserService()

@user_bp.route('/', methods=['GET'])
def list_all():
    result = service.get()

    data = []

    for c in result:
        value = {
            "id": c.id, 
            "name": c.name,  
            "email": c.email,
            "role": c.role, 
            "is_active": c.is_active, 
            "created_at": c.created_at, 
        }
        data.append(value)

    return data


@user_bp.route('/<int:id_user>', methods=['GET'])
def list_one(id_user):
    try:
        result = service.getById(id_user)

        data = [
            {
                "id": result.id, 
                "name": result.name,  
                "email": result.email,
                "role": result.role, 
                "is_active": result.is_active, 
                "created_at": result.created_at, 
            }
        ]

        return data
    except Exception:
        
        return result


@user_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@user_bp.route('/update/<int:id_user>', methods=['POST'])
def update(id_user):
    data = request.form.to_dict()

    result = service.update(data, id_user)

    return result

@user_bp.route('/delete/<int:id_user>', methods=['POST'])
def delete(id_user):
    
    result = service.delete(id_user)

    return result