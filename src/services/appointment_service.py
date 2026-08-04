from src.models.appointment import Appointment
from src.models.user import User
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.package import Package

class AppointmentService:

    def get(self):
        data = Appointment.select()

        return data
    

    def getById(self, id_appointment: int):
        appointment_id = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment_id:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment = {
            "id": appointment_id.id,
            "customer_id": appointment_id.customer_id_id,
            "pet_id": appointment_id.pet_id_id,
            "package_id": appointment_id.service_id_id,
            "user_id": appointment_id.user_id_id,
            "scheduled_at": appointment_id.scheduled_at,
            "status": appointment_id.status,
            "notes": appointment_id.notes,
        }

        return appointment


    def create(self, data):

        customer = Customer.get_or_none(
            Customer.id == data['customer_id']
        )

        pet = Pet.get_or_none(
            Pet.id == data['pet_id']
        )

        package = Package.get_or_none(
            Package.id == data['package_id']
        )

        user = User.get_or_none(
            User.id == data['user_id']
        )

        if not customer:
            return {"message": "Cliente e obrigatório para agendamento!!!", "status": False}
        
        if not pet:
            return {"message": "Pet e obrigatório para agendamento!!!", "status": False}
        
        if not package:
            return {"message": "Serviço e obrigatório para agendamento!!!", "status": False}
        
        if not user:
            return {"message": "Usuário e obrigatório para agendamento!!!", "status": False}
        

        Appointment.create(
            customer_id = customer,
            pet_id = pet,
            package_id = package,
            user_id = user,
            scheduled_at = data['scheduled_at'],
            status = data['status'] or 'in_progress',
            notes = data['notes'],
        )

        return {"message": "Agendamento registrado com sucesso!!!", "status": True}
        

    def update(self, data, id_appointment: int):

        appointment = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        customer = Customer.get_or_none(
            Customer.id == data['customer_id']
        )

        pet = Pet.get_or_none(
            Pet.id == data['pet_id']
        )

        package = Package.get_or_none(
            Package.id == data['package_id']
        )

        user = User.get_or_none(
            User.id == data['user_id']
        )

        if not appointment:
            return {"message": "agendamento não encontrado!!!", "status": False}

        if not customer:
            return {"message": "Cliente e obrigatório para agendamento!!!", "status": False}
        
        if not pet:
            return {"message": "Pet e obrigatório para agendamento!!!", "status": False}
        
        if not package:
            return {"message": "Serviço e obrigatório para agendamento!!!", "status": False}
        
        if not user:
            return {"message": "Usuário e obrigatório para agendamento!!!", "status": False}

        appointment.customer_id = customer
        appointment.pet_id = pet
        appointment.package_id_id = package
        appointment.user_id = user
        appointment.scheduled_at = data['scheduled_at']
        appointment.status = data['status']
        appointment.notes = data['notes']

        appointment.save()

        return {
            "message": "Agendamento atualizado com sucesso",
            "status": True
        }

    def delete(self, id_appointment: int):

        appointment = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment:
            return {"message": "Agendamento não encontrado!!!", "status": False}

        appointment.delete_instance()

        return {
            "message": "Agendamento removido com sucesso",
            "status": True
        }
