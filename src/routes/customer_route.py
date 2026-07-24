from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

service = CustomerService()

""" RENDERIZAÇÃO DE TELAS """

@customer_bp.route('/form-add', methods=['GET'])
def form_add():

     return render_template("customer/add_customer.html")


""" ROTAS DE CRUD """

@customer_bp.route('/', methods=['GET'])
def list_all():

    try:
        customers = service.get()

        return render_template("index/index.html", tab="customers", customers=customers)
    except Exception as e:
        return str(e), 500


@customer_bp.route('/<int:id_customer>', methods=['GET'])
def list_one(id_customer: int):
    
    try:
        customer = service.getById(id_customer)

        print(customer['is_active'])

        return render_template("customer/info_customer.html", customer=customer)
    except Exception as e:
        
        return str(e), 500

    
@customer_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = service.create(data)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('index.index', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="customers"))


@customer_bp.route('/update/<int:id_customer>', methods=['POST'])
def update(id_customer):
    data = request.form.to_dict()

    result = service.update(data, id_customer)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('index.index', tab="customers"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="customers"))



@customer_bp.route('/delete/<int:id_customer>', methods=['POST'])
def delete(id_customer):

    result = service.delete(id_customer)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('index.index', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="customers"))