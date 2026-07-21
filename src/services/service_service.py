from src.models.service import Service


class ServiceService:

    def get(self):
        data = Service.select()

        return data
    

    def getById(self, id_service: int):
        service_id = Service.get_or_none(
            Service.id == id_service
        )

        if not service_id:
            return {"error": "Serviço não encontrado!!!"}
        
        service = {
            "id": service_id.id,
            "name": service_id.name,
            "notes": service_id.notes,
            "price_small": service_id.price_small,
            "price_medium": service_id.price_medium,
            "price_large": service_id.price_large,
            "create_at": service_id.created_at
        }

        return service


    def create(self, data):

        if data['name'] == '':
            return {"error": "O nome do serviço e obrigatório"}, 404

        Service.create(
            name = data['name'],
            notes = data['notes'],
            price_small = data['price_small'],
            price_medium = data['price_medium'],
            price_large = data['price_large'],
        )

        return {"message": "Serviço cadastrado com sucesso"}, 201


    def update(self, data, id_service: int):

        service = Service.get_or_none(
            Service.id == id_service
        )

        if not service:
            return {"error": "Serviço não encontrado"}

        if data['name'] == '':
            return {"error": "Nome do Serviço e Obrigatório"}

        service.name = data['name']
        service.notes = data['notes']
        service.price_small = data['price_small']
        service.price_medium = data['price_medium']
        service.price_large = data['price_large']

        service.save()

        return {
            "message": "Serviço atualizado com sucesso"
        }

    def delete(self, id_service: int):

        service = Service.get_or_none(
            Service.id == id_service
        )

        if not service:
            return {"error": "Serviço não encontrado!!!"}

        service.delete_instance()

        return {
            "message": "Serviço removido com sucesso"
        }
