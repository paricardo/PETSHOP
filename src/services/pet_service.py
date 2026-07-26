from src.models.pet import Pet
from src.models.customer import Customer
from werkzeug.utils import secure_filename
import os


class PetService:

    def get(self):
        data = Pet.select()

        return data
    

    def getById(self, id_pet: int):

        pet_id = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet_id:
            return {"message": "Pet não encontrado!!!", "status": False}
        
        pet = {
            "id": pet_id.id,
            "name": pet_id.name,
            "breed": pet_id.breed,
            "notes": pet_id.notes,
            "is_active": pet_id.is_active,
            "created_at": pet_id.created_at,
            "photo": pet_id.photo,
        }

        return pet


    def create(self, data, photo):

        customer_id = Customer.get_or_none(
            Customer.id == data["customer_id"]
        )

        if not customer_id:
            return {"message": "Pet não encontrado!!!", "status": False}

        if not data["name"]:
            return {"message": "Nome do pet é obrigatório!!!", "status": False}

        UPLOAD_FOLDER = "src/static/uploads"

        # Imagem padrão
        filename = "img-pet.png"

        # Se o usuário enviou uma imagem
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(UPLOAD_FOLDER, filename))

        Pet.create(
            name=data["name"],
            breed=data["breed"],
            notes=data["notes"],
            customer_id=data["customer_id"],
            photo=filename
        )

        return {"message": "Pet cadastrado com sucesso", "status": True}


    def update(self, data, id_pet: int):

        pet = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet:
            return {"message": "Serviço não encontrado", "status": False}

        pet.name = data['name']
        pet.breed = data['breed']
        pet.notes = data['notes']
        pet.is_active = data['is_active']

        pet.save()

        return {"message": "Pet atualizado com sucesso", "status": True}

    def delete(self, id_pet: int):

        pet = Pet.get_or_none(
            Pet.id == id_pet
        )

        if not pet:
            return {"error": "Pet não encontrado!!!", "status": False}

        pet.delete_instance()

        return {
            "message": "pet removido com sucesso",
            "status": True
        }
