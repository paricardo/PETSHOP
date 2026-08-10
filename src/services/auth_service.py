from src.models.user import User
from werkzeug.security import check_password_hash

class AuthService:

    def authenticate(self, email, password):

        user = User.get_or_none(
            User.email == email
        )

        if not user:
            return {
                "status": False,
                "message": "Usuário não encontrado!"
            }
        

        if not check_password_hash(user.password, password):
            return {
                "status": False,
                "message": "Senha incorreta!"
            }

        return {
            "status": True,
            "id": user.id,
            "name": user.name
        }