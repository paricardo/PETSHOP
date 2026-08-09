from src.services.appointment_service import AppointmentService
from src.services.customer_service import CustomerService
from src.services.user_service import UserService
from src.services.package_service import PackageService
from src.services.pet_service import PetService
from flask import (
    Blueprint, 
    request, 
    render_template,
    redirect,
    url_for,
    flash
)

appointment_bp = Blueprint('appointment', __name__)

appointment_service = AppointmentService()
customer_service = CustomerService()
user_service = UserService()
package_service = PackageService()
pet_service = PetService()

""" ROTAS DE CRUD """


@appointment_bp.route("/search", methods=['GET', 'POST'])
def search_appointments():
    query = request.form.get('search', '') or request.args.get('query', '')
    query = query.strip()

    if query:
        appointments = appointment_service.search(query)
    else:
        appointments = []

    return render_template(
        "appointment/appointment.html",
        appointments=appointments,
        search_query=query,
    )

@appointment_bp.route('/completed-appointments/<int:id_appointment>', methods=['GET', 'POST'])
def completed_appointments(id_appointment: int):

    result = appointment_service.completed_appointments(id_appointment)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('home.index'))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('home.index'))
    

@appointment_bp.route('/form-add/<int:customer_id>', methods=['GET'])
def form_add(customer_id: int):

    customer = customer_service.getById(customer_id)
    users = user_service.get()
    packages = package_service.get()

    return render_template('appointment/add_appointment.html', 
                           customer=customer,
                           users=users,
                           packages=packages
                           )


@appointment_bp.route('/', methods=['GET'])
def list_all():
    appointments = appointment_service.get()
    customers = customer_service.get()
    packages = package_service.get()
    
    return render_template("appointment/appointment.html", 
                            appointments=appointments,
                            customers=customers,
                            packages=packages)


@appointment_bp.route('/<int:id_appointment>', methods=['GET'])
def list_one(id_appointment: int):
    
    appointment = appointment_service.getById(id_appointment)

    user = user_service.getById(appointment['user_id'])
    customer = customer_service.getById(appointment['customer_id'])
    package = package_service.getById(appointment['package_id'])
    pet = pet_service.getById(appointment['pet_id'])

    USERS = user_service.get()
    PACKAGES = package_service.get()

    return render_template('appointment/info_appointment.html',
                            appointment=appointment,    
                            user=user,
                            customer=customer,
                            package=package,
                            pet=pet,
                            USERS=USERS,
                            PACKAGES=PACKAGES
                        )

    
@appointment_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = appointment_service.create(data)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('home.index'))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('home.index'))


@appointment_bp.route('/update/<int:id_appointment>', methods=['POST'])
def update(id_appointment):
    data = request.form.to_dict()

    result = appointment_service.update(data, id_appointment)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('home.index'))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('home.index'))


@appointment_bp.route('/delete/<int:id_appointment>', methods=['POST'])
def delete(id_appointment):

    result = appointment_service.delete(id_appointment)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('home.index'))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('home.index'))