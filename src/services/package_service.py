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
            return {"error": "pacote não encontrado!!!"}
        
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

        if data['name'] == '':
            return {"error": "O nome do pacote e obrigatório"}, 404

        Package.create(
            name = data['name'],
            services = data['services'],
            price_small = data['price_small'],
            price_medium = data['price_medium'],
            price_large = data['price_large'],
        )

        return {"message": "Pacote cadastrado com sucesso"}, 201


    def update(self, data, id_package: int):

        package = Package.get_or_none(
            Package.id == id_package
        )

        if not package:
            return {"error": "Pacote não encontrado"}

        if data['name'] == '':
            return {"error": "Nome do Pacote e Obrigatório"}

        package.name = data['name']
        package.services = data['services']
        package.price_small = data['price_small']
        package.price_medium = data['price_medium']
        package.price_large = data['price_large']

        package.save()

        return {
            "message": "Pacote atualizado com sucesso"
        }

    def delete(self, id_package: int):

        package = Package.get_or_none(
            Package.id == id_package
        )

        if not package:
            return {"error": "Pacote não encontrado!!!"}

        package.delete_instance()

        return {
            "message": "Pacote removido com sucesso"
        }
