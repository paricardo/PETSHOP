from src.services.package_service import PackageService
from flask import (
    Blueprint, 
    request, 
    render_template,
    url_for,
    redirect,
    flash
)

package_bp = Blueprint('package', __name__)

service = PackageService()

@package_bp.route('/form-add', methods=['GET'])
def form_add():

     return render_template("package/add_package.html")

""" ROTAS DE CRUD """

@package_bp.route('/', methods=['GET'])
def list_all():
    try:
        packages = service.get()

        return render_template("index/index.html", tab="packages", packages=packages)
    except Exception as e:
        return str(e), 500


@package_bp.route('/<int:id_package>', methods=['GET'])
def list_one(id_package: int):
    
    try:
        package = service.getById(id_package)

        return render_template("package/info_package.html", package=package)
    except Exception as e:
        
        return str(e), 500

    
@package_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()
    
    result = service.create(data)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('index.index', tab="packages"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="packages"))


@package_bp.route('/update/<int:id_package>', methods=['POST'])
def update(id_package):
    data = request.form.to_dict()
    
    result = service.update(data, id_package)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('index.index', tab="packages"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="packages"))


@package_bp.route('/delete/<int:id_package>', methods=['POST'])
def delete(id_package):

    result = service.delete(id_package)
    
    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('index.index', tab="packages"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('index.index', tab="packages"))