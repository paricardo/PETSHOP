from src.models.customer import Customer
from src.utils.validators import (
    format_phone,
    validate_email
)

class CustomerService:

    def get(self):
        ...
    

    def getById(self):
        ...


    def create(self, data):

        valid_email = validate_email(data['email']) 

        if not valid_email:
            return {"error": "Email Invalido!!!"}
        
        phone, status = format_phone(data['phone']) 

        if status == False:
            return {"error": "Telefone Invalido!!!"}, 404

        Customer.create(
            name = data['name'],
            phone = phone,
            email = data.get('email') or None,
            address = data['address'],
            notes = data.get('notes'),
        )

        return {"message": "Cliente cadastrado com sucesso"}


    def update(self, data, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"error": "Cliente não encontrado"}

        if not validate_email(data["email"]):
            return {"error": "Email inválido"}

        phone, status = format_phone(data["phone"])

        if not status:
            return {"error": "Telefone inválido"}

        customer.name = data["name"]
        customer.phone = phone
        customer.email = data["email"] or None
        customer.address = data["address"]
        customer.notes = data["notes"] or None

        customer.save()

        return {
            "message": "Cliente atualizado com sucesso"
        }

    def delete(self, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"error": "Cliente não encontrado!!!"}

        customer.delete_instance()

        return {
            "message": "Cliente removido com sucesso"
        }