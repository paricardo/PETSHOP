from src.models.appointment import Appointment
from src.models.user import User
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.service import Service

class AppointmentService:

    def get(self):
        data = Appointment.select()

        return data
    

    def getById(self, id_appointment: int):
        appointment_id = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment_id:
            return {"error": "Agendamento não encontrado"}, 404
        
        appointment = {
            "id": appointment_id.id,
            "customer_id": appointment_id.customer_id_id,
            "pet_id": appointment_id.pet_id_id,
            "service_id": appointment_id.service_id_id,
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

        service = Service.get_or_none(
            Service.id == data['service_id']
        )

        user = User.get_or_none(
            User.id == data['user_id']
        )

        if not customer:
            return {"error": "Cliente e obrigatório para agendamento!!!"}, 404
        
        if not pet:
            return {"error": "Pet e obrigatório para agendamento!!!"}, 404
        
        if not service:
            return {"error": "Serviço e obrigatório para agendamento!!!"}, 404
        
        if not user:
            return {"error": "Usuário e obrigatório para agendamento!!!"}, 404
        

        Appointment.create(
            customer_id = customer,
            pet_id = pet,
            service_id = service,
            user_id = user,
            scheduled_at = data['scheduled_at'],
            status = data['status'] or 'in_progress',
            notes = data['notes'],
        )

        return {"error": "Agendamento registrado com sucesso!!!"}, 201
        

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

        service = Service.get_or_none(
            Service.id == data['service_id']
        )

        user = User.get_or_none(
            User.id == data['user_id']
        )

        if not appointment:
            return {"error": "agendamento não encontrado!!!"}, 404

        if not customer:
            return {"error": "Cliente e obrigatório para agendamento!!!"}, 404
        
        if not pet:
            return {"error": "Pet e obrigatório para agendamento!!!"}, 404
        
        if not service:
            return {"error": "Serviço e obrigatório para agendamento!!!"}, 404
        
        if not user:
            return {"error": "Usuário e obrigatório para agendamento!!!"}, 404

        appointment.customer_id = customer
        appointment.pet_id = pet
        appointment.service_id = service
        appointment.user_id = user
        appointment.scheduled_at = data['scheduled_at']
        appointment.status = data['status']
        appointment.notes = data['notes']

        appointment.save()

        return {
            "message": "Agendamento atualizado com sucesso"
        }, 200

    def delete(self, id_appointment: int):

        appointment = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment:
            return {"error": "Agendamento não encontrado!!!"}

        appointment.delete_instance()

        return {
            "message": "Agendamento removido com sucesso"
        }, 200
