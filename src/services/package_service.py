from src.models.package import Package


class PackageService:

    def get(self):
        data = Package.select()

        return data
    

    def getById(self, id_package: int):
        package_id = Package.get_or_none(
            Package.id == id_package
        )

        if not package_id:
            return {"message": "pacote não encontrado!!!", "status": False}
        
        package = {
            "id": package_id.id,
            "name": package_id.name,
            "services": package_id.services,
            "price_small": package_id.price_small,
            "price_medium": package_id.price_medium,
            "price_large": package_id.price_large,
            "create_at": package_id.created_at
        }

        return package


    def create(self, data):

        if not data['name']:
            return {"message": "O nome do pacote e obrigatório", "status": False}

        if not data['services']:
            return {"message": "Os serviços do pacote são obrigatórios!!!", "status": False}

        if not data['price_small']:
            return {"message": "O preço para porte pequeno e obrigatório!!!", "status": False}

        Package.create(
            name = data['name'],
            services = data['services'],
            price_small = data['price_small'],
            price_medium = data['price_medium'],
            price_large = data['price_large'],
            quantity = data['quantity']
        )

        return {"message": "Pacote cadastrado com sucesso", "status": True}


    def update(self, data, id_package: int):

        package = Package.get_or_none(
            Package.id == id_package
        )

        if not package:
            return {"message": "Pacote não encontrado", "status": False}

        if not data['name']:
            return {"message": "O nome do pacote e obrigatório", "status": False}

        if not data['services']:
            return {"message": "Os serviços do pacote são obrigatórios!!!", "status": False}

        if not data['price_small']:
            return {"message": "O preço para porte pequeno e obrigatório!!!", "status": False}

        package.name = data['name']
        package.services = data['services']
        package.price_small = data['price_small']
        package.price_medium = data['price_medium']
        package.price_large = data['price_large']
        package.quantity = data['quantity']

        package.save()

        return {
            "message": "Pacote atualizado com sucesso",
            "status": True
        }

    def delete(self, id_package: int):

        package = Package.get_or_none(
            Package.id == id_package
        )

        if not package:
            return {"message": "Pacote não encontrado!!!", "status": False}

        package.delete_instance()

        return {
            "message": "Pacote removido com sucesso",
            "status": True
        }
