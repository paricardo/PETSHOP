from src.models.customer import Customer
from src.utils.validators import (
    format_phone,
    validate_email
)

class CustomerService:

    def get(self):
        data = Customer.select()

        return data
    

    def getById(self, id_customer: int):
        
        customer = Customer.get_or_none(
            Customer.id == id_customer
        )
       
        if not customer:
            return {"error": "Cliente não encontrado!!!"}

        return customer


    def create(self, data):

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"error": "Email invalido!!!"}, 404
        
        if not data['name']:
            return {"error": "O nome do cliente e obrigatório!!!"}
        
        phone, status = format_phone(data['phone']) 

        if status == False:
            return {"error": "Telefone Invalido!!!"}, 404

        Customer.create(
            name = data['name'],
            phone = phone,
            email = email or '',
            address = data['address'],
            notes = data.get('notes'),
        )

        return {"message": "Cliente cadastrado com sucesso"}, 201


    def update(self, data, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"error": "Cliente não encontrado"}, 404

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"error": "Email invalido!!!"}, 404
        
        if not data['name']:
            return {"error": "O nome do cliente e obrigatório!!!"}

        valid_phone, status = format_phone(data["phone"])

        if status == False:
            {"error": "Telefone invalido!!!"}, 404

        if status == True:
            phone = valid_phone

        customer.name = data["name"]
        customer.phone = phone
        customer.email = email or ''
        customer.address = data["address"]
        customer.notes = data["notes"] or None

        customer.save()

        return {
            "message": "Cliente atualizado com sucesso"
        }, 200

    def delete(self, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"error": "Cliente não encontrado!!!"}, 404

        customer.delete_instance()

        return {
            "message": "Cliente removido com sucesso"
        }, 200
