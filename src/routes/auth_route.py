from flask import (
    Blueprint, 
    render_template, 
    request,
    session,
    flash,
    url_for,
    redirect
)
from src.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

auth_service = AuthService()


@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    return render_template("login/login.html")


@auth_bp.route("/auth", methods=["POST"])
def auth():
    email = request.form.get("email")
    password = request.form.get("password")

    result = auth_service.authenticate(email, password)

    if result["status"] is False:
        flash(result["message"], "danger")
        return redirect(url_for("auth.login"))

    session["user_id"] = result["id"]
    session["user_name"] = result["name"]
    session["user_role"] = result["role"]

    return redirect(url_for("home.index"))


@auth_bp.route("/logout")
def logout():
    session.clear()

    flash("Você saiu do sistema.", "success")

    return redirect(url_for("auth.login"))