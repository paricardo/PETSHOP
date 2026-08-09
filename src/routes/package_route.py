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

package_service = PackageService()

@package_bp.route('/form-add', methods=['GET'])
def form_add():

     return render_template("package/add_package.html")

@package_bp.route('/search', methods=['POST'])
def search_package():
    query = request.form.get('search', '') or request.args.get('query', '')
    query = query.strip()

    if query:
        packages = package_service.search(query)
    else:
        packages = []

    return render_template(
        "package/package.html",
        packages=packages,
        search_query=query,
    )

""" ROTAS DE CRUD """

@package_bp.route('/', methods=['GET'])
def list_all():
    try:
        packages = package_service.get()

        return render_template("package/package.html", tab="packages", packages=packages)
    except Exception as e:
        return str(e), 500


@package_bp.route('/<int:id_package>', methods=['GET'])
def list_one(id_package: int):
    
    try:
        package = package_service.getById(id_package)

        return render_template("package/info_package.html", package=package)
    except Exception as e:
        
        return str(e), 500

    
@package_bp.route('/add', methods=['POST'])
def create():
    data = request.form.to_dict()
    
    result = package_service.create(data)

    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('package.list_all', tab="packages"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('package.list_all', tab="packages"))


@package_bp.route('/update/<int:id_package>', methods=['POST'])
def update(id_package):
    data = request.form.to_dict()
    
    result = package_service.update(data, id_package)

    if result['status'] == True:
        flash(result['message'], "success")
        return redirect(url_for('package.list_all', tab="packages"))

    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('package.list_all', tab="packages"))


@package_bp.route('/delete/<int:id_package>', methods=['POST'])
def delete(id_package):

    result = package_service.delete(id_package)
    
    if result['status'] == True:
            flash(result['message'], "success")
            return redirect(url_for('package.list_all', tab="packages"))
    
    if result['status'] == False:
        flash(result['message'], "danger")
        return redirect(url_for('package.list_all', tab="packages"))