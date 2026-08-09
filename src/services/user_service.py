from src.models.user import User
from werkzeug.security import generate_password_hash
from src.utils.validators import validate_email

class UserService:

    def search(self, query: str):
        users = User.select().where(
            (User.name.contains(query)) |
            (User.email.contains(query))
        )

        return users

    def get(self):
        data = User.select()

        return data
    

    def getById(self, id_user: int):
        
        user_id = User.get_or_none(
            User.id == id_user
        )
       
        if not user_id:
            return {"message": "Usuário não encontrado!!!", "status": False}
                
        user = {
            "id": user_id.id,
            "name": user_id.name,
            "email": user_id.email,
            "role": user_id.role,
            "is_active": user_id.is_active,
            "created_at": user_id.created_at
        }

        return user


    def create(self, data):

        if not data['email']:
            return {"message": "Email do usuário e obrigatório", "status": False}

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"message": "Email invalido!!!", "status": False}
        
        if not data['name']:
            return {"message": "O nome do usuário e obrigatório!!!", "status": False}

        if not data['password']:
            return {"message": "O campo senha e obrigatório ...", "status": False}
    

        User.create(
            name = data['name'],
            email = email,
            password = generate_password_hash(data['password']),
            role = data['role'],
        )

        return {"message": "Usuario cadastrado com sucesso", "status": True}


    def update(self, data, id_user: int):

        user = User.get_or_none(
            User.id == id_user
        )

        if not data['email']:
            return {"message": "Email do usuário e obrigatório", "status": False}

        if not user:
            return {"message": "Usuário não encontrado", "status": False}

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"message": "Email invalido!!!", "status": False}
        
        if not data['name']:
            return {"message": "O nome do usuário e obrigatório!!!", "status": False}


        user.name = data["name"]
        user.email = email
        user.password = generate_password_hash(data['password']) 
        user.role = data['role'] or "Admin"
        user.is_active = data['is_active']

        user.save()

        return {
            "message": "Usuário atualizado com sucesso",
            "status": True
        }

    def delete(self, id_user: int):

        user = User.get_or_none(
            User.id == id_user
        )

        if not user:
            return {"message": "Usuário não encontrado!!!", "status": False}

        user.delete_instance()

        return {
            "message": "Usuário removido com sucesso",
            "status": True
        }
