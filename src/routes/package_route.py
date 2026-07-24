from flask import Blueprint, request
from src.services.package_service import PackageService

package_bp = Blueprint('package', __name__)

service = PackageService()

""" ROTAS DE CRUD """

@package_bp.route('/', methods=['GET'])
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


@package_bp.route('/<int:id_service>', methods=['GET'])
def list_one(id_package: int):
    
    try:
        result = service.getById(id_package)

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

    
@package_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    return result


@package_bp.route('/update/<int:id_service>', methods=['POST'])
def update(id_package):
    data = request.form.to_dict()

    result = service.update(data, id_package)

    return result


@package_bp.route('/delete/<int:id_service>', methods=['POST'])
def delete(id_package):

    result = service.delete(id_package)

    return result