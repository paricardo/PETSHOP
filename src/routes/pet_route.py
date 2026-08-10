from src.services.pet_service import PetService
from src.services.customer_service import CustomerService
from src.utils.decorators.auth_decorator import login_required
from flask import Blueprint, request, flash, url_for, redirect, render_template

pet_bp = Blueprint('pet', __name__)

service = PetService()

customerService = CustomerService()

@pet_bp.route('/form-add/<int:id_customer>', methods=['GET', 'POST'])
@login_required
def form_add(id_customer):
    customer = customerService.getById(id_customer)    

    return render_template("pet/add_pet.html" , customer=customer )

@pet_bp.route('/', methods=['GET'])
@login_required
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
@login_required
def list_one(id_pet):

    pet = service.getById(id_pet)

    if pet.get("status") is False:
        flash(pet["message"], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))

    try:
        return render_template("pet/info_pet.html", pet=pet)
    except Exception as e:
        print(e)
        raise


@pet_bp.route('/add', methods=['POST'])
@login_required
def create():
    data = request.form.to_dict()

    photo = request.files.get("photo")

    result = service.create(data, photo)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('customer.list_all', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))


@pet_bp.route('/update/<int:id_pet>', methods=['POST'])
@login_required
def update(id_pet):
    data = request.form.to_dict()

    result = service.update(data, id_pet)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('customer.list_all', tab="customers"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))

@pet_bp.route('/delete/<int:id_pet>', methods=['POST'])
@login_required
def delete(id_pet):
    
    result = service.delete(id_pet)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('customer.list_all', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))