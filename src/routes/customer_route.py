from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

customer_service = CustomerService()

""" RENDERIZAÇÃO DE TELAS """

@customer_bp.route('/form-add', methods=['GET'])
def form_add():

     return render_template("customer/add_customer.html")


@customer_bp.route("/search", methods=['GET', 'POST'])
def search_customers():
    query = request.form.get('search', '') or request.args.get('query', '')
    query = query.strip()

    if query:
        customers = customer_service.search(query)
    else:
        customers = []

    return render_template(
        "customer/customer.html",
        customers=customers,
        search_query=query,
    )


""" ROTAS DE CRUD """

@customer_bp.route('/', methods=['GET'])
def list_all():

    try:
        customers = customer_service.get()

        return render_template("customer/customer.html", tab="customers", customers=customers)
    except Exception as e:
        return str(e), 500


@customer_bp.route('/<int:id_customer>', methods=['GET'])
def list_one(id_customer: int):
    
    try:
        customer = customer_service.getById(id_customer)

        return render_template("customer/info_customer.html", customer=customer)
    except Exception as e:
        
        return str(e), 500

    
@customer_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()

    result = customer_service.create(data)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('customer.list_all', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))


@customer_bp.route('/update/<int:id_customer>', methods=['POST'])
def update(id_customer):
    data = request.form.to_dict()

    result = customer_service.update(data, id_customer)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('customer.list_all', tab="customers"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))



@customer_bp.route('/delete/<int:id_customer>', methods=['POST'])
def delete(id_customer):

    result = customer_service.delete(id_customer)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('customer.list_all', tab="customers"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('customer.list_all', tab="customers"))