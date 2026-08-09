from src.services.user_service import UserService
from flask import (
    Blueprint, 
    request, 
    render_template,
    flash,
    url_for,
    redirect
)

user_bp = Blueprint('user', __name__)

user_service = UserService()

@user_bp.route('/form-add', methods=['GET'])
def form_add():

     return render_template("user/add_user.html")


@user_bp.route("/search", methods=['GET', 'POST'])
def search_users():
    query = request.form.get('search', '') or request.args.get('query', '')
    query = query.strip()

    if query:
        users = user_service.search(query)
    else:
        users = []

    return render_template(
        "user/user.html",
        users=users,
        search_query=query,
    )



@user_bp.route('/', methods=['GET'])
def list_all():
    try:
        users = user_service.get()

        return render_template("user/user.html", tab="user", users=users)
    except Exception as e:
        return str(e), 500


@user_bp.route('/<int:id_user>', methods=['GET'])
def list_one(id_user):
    try:
        user = user_service.getById(id_user)

        return render_template("user/info_user.html", user=user)
    except Exception as e:
        
        return str(e), 500


@user_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()
        
    result = user_service.create(data)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('user.list_all', tab="user"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('user.list_all', tab="user"))


@user_bp.route('/update/<int:id_user>', methods=['POST'])
def update(id_user):
    data = request.form.to_dict()
        
    result = user_service.update(data, id_user)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('user.list_all', tab="user"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('user.list_all', tab="user"))

@user_bp.route('/delete/<int:id_user>', methods=['POST'])
def delete(id_user):
    
    result = user_service.delete(id_user)
        
    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('user.list_all', tab="user"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('user.list_all', tab="user"))