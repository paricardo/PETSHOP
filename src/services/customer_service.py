from src.models.customer import Customer
from src.models.pet import Pet
from src.utils.validators import (
    format_phone,
    validate_email
)

class CustomerService:

    def search(self, query: str):
        customers = Customer.select().where(
            (Customer.name.contains(query)) |
            (Customer.phone.contains(query)) |
            (Customer.email.contains(query))
        )

        return customers

    def get(self):
        data = Customer.select()

        return data
    

    def getById(self, id_customer: int):
        
        customer_id = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer_id:
            return {"message": "Cliente não encontrado!!!", "status": False}
        

        customer = {
            "id": customer_id.id,
            "name": customer_id.name, 
            "phone": customer_id.phone,
            "email": customer_id.email,
            "address": customer_id.address,
            "notes": customer_id.notes,
            "is_active": customer_id.is_active,
            "created_at": customer_id.created_at,
            "pets": []
        }
        

        pets = Pet.select().where(
            Pet.customer_id == customer_id
        )

        for pet in pets:
            customer["pets"].append({
                "id": pet.id,
                "name": pet.name,
                "breed": pet.breed,
                "notes": pet.notes,
                "is_active": pet.is_active,
                "created_at": pet.created_at,
                "photo": pet.photo,
            })

        return customer


    def create(self, data):

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if Customer.select().where(Customer.email == email).exists():
            return {"message": "Email já cadastrado!!!", "status": False}

        if valid_email == False:
            return {"message": "Email invalido!!!", "status": False}
        
        if not data['name']:
            return {"message": "O nome do cliente e obrigatório!!!", "status": False}
        
        phone, status = format_phone(data['phone']) 

        if status == False:
            return {"message": "Telefone Invalido!!!", "status": False}

        if Customer.select().where(Customer.phone == phone).exists():
            return {"message": "Telefone já cadastrado!!!", "status": False}


        Customer.create(
            name = data['name'],
            phone = phone,
            email = email or '',
            address = data['address'],
            notes = data.get('notes'),
            is_active = True,
        )

        return {"message": "Cliente cadastrado com sucesso", "status": True}


    def update(self, data, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"message": "Cliente não encontrado", "status": False}

        valid_email = validate_email(data['email']) 

        if valid_email == True:
            email = data['email']

        if valid_email == False:
            return {"message": "Email invalido!!!", "stats": False}
        
        if not data['name']:
            return {"message": "O nome do cliente e obrigatório!!!", "status": False}

        valid_phone, status = format_phone(data["phone"])

        if status == False:
            {"message": "Telefone invalido!!!", "status": False}
        if status == True:
            phone = valid_phone

        if data['is_active'] == "True":
            is_active = True
        else:
            is_active = False

        customer.name = data["name"]
        customer.phone = phone
        customer.email = email or ''
        customer.address = data["address"]
        customer.notes = data["notes"] or None
        customer.is_active = is_active

        customer.save()

        return {"message": "Cliente atualizado com sucesso", "status": True}
    
    def delete(self, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"message": "Cliente não encontrado!!!", "status": False}
        customer.delete_instance()

        return {"message": "Cliente removido com sucesso", "status": True}
