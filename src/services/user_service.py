from src.models.user import User
from werkzeug.security import generate_password_hash
from src.utils.validators import validate_email

class UserService:

    def get(self):
        data = User.select()

        return data
    

    def getById(self, id_user: int):
        
        user = User.get_or_none(
            User.id == id_user
        )
       
        if not user:
            return {"error": "Usuário não encontrado!!!"}

        return user


    def create(self, data):

        if not data['email']:
            return {"error": "Email do usuário e obrigatório"}, 404

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"error": "Email invalido!!!"}, 404
        
        if not data['name']:
            return {"error": "O nome do usuário e obrigatório!!!"}, 404
    

        User.create(
            name = data['name'],
            email = email,
            password = generate_password_hash(data['password']),
            role = data['role'],
        )

        return {"message": "Usuario cadastrado com sucesso"}, 201


    def update(self, data, id_user: int):

        user = User.get_or_none(
            User.id == id_user
        )

        if not data['email']:
            return {"error": "Email do usuário e obrigatório"}, 404

        if not user:
            return {"error": "Usuário não encontrado"}, 404

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"error": "Email invalido!!!"}, 404
        
        if not data['name']:
            return {"error": "O nome do usuário e obrigatório!!!"}, 404


        user.name = data["name"]
        user.email = email
        user.password = generate_password_hash(data['password']) 
        user.role = data['role']
        user.is_active = data['is_active']

        user.save()

        return {
            "message": "Usuário atualizado com sucesso"
        }, 200

    def delete(self, id_user: int):

        user = User.get_or_none(
            User.id == id_user
        )

        if not user:
            return {"error": "Usuário não encontrado!!!"}, 404

        user.delete_instance()

        return {
            "message": "Usuário removido com sucesso"
        }, 200
