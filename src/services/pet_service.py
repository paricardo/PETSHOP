from src.models.pet import Pet
from src.models.customer import Customer


class PetService:

    def get(self):
        data = Pet.select()

        return data
    

    def getById(self, id_pet: int):

        pet_id = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet_id:
            return {"error": "Pet não encontrado!!!"}
        
        pet = {
            "name": pet_id.name,
            "breed": pet_id.breed,
            "notes": pet_id.notes,
            "is_active": pet_id.is_active,
            "created_at": pet_id.created_at,
            "customer_id": pet_id.customer_id_id
        }

        return pet


    def create(self, data):

        customer_id = Customer.get_or_none(
            Customer.id == data['customer_id']
        )

        if not customer_id:
            return {"error": "Cliente não encontrado!!!"}, 404
        
        if not data['name']:
            return {"error": "Nome do pet e obrigatório!!!"}, 404

        Pet.create(
            name = data['name'],
            breed = data['breed'],
            notes = data['notes'],

            customer_id = data['customer_id'],
        )

        return {"message": "Pet cadastrado com sucesso"}, 201


    def update(self, data, id_pet: int):

        pet = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet:
            return {"error": "Serviço não encontrado"}, 404

        pet.name = data['name']
        pet.breed = data['breed']
        pet.notes = data['notes']
        pet.is_active = data['is_active']

        pet.save()

        return {
            "message": "Pet atualizado com sucesso"
        }, 200

    def delete(self, id_pet: int):

        pet = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet:
            return {"error": "Pet não encontrado!!!"}, 404

        pet.delete_instance()

        return {
            "message": "pet removido com sucesso"
        }, 200
