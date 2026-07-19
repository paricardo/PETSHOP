from src.models.appointment import Appointment
from src.models.user import User


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
            "customer_id": appointment_id.customer_id,
            "pet_id": appointment_id.pet_id,
            "service_id": appointment_id.service_id,
            "user_id": appointment_id.user_id,
            "scheduled_at": appointment_id.scheduled_at,
            "status": appointment_id.status,
            "notes": appointment_id.notes,
        }

        return appointment


    def create(self, data):

        if not data['customer_id']:
            return {"error": "Cliente e obrigatório para agendamento!!!"}, 404
        
        if not data['pet_id']:
            return {"error": "Pet e obrigatório para agendamento!!!"}, 404
        
        if not data['service_id']:
            return {"error": "Serviço e obrigatório para agendamento!!!"}, 404
        
        if not data['user_id']:
            return {"error": "Usuário e obrigatório para agendamento!!!"}, 404
        

        Appointment.create(
            customer_id = data['customer_id'],
            pet_id = data['pet_id'],
            service_id = data['service_id'],
            user_id = data['user_id'],
            scheduled_at = data['scheduled_at'],
            status = data['status'],
            notes = data['notes'],
        )

        return {"error": "Agendamento registrado com sucesso!!!"}, 201
        

    def update(self, data, id_appointment: int):

        appointment = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment:
            return {"error": "Agendamento não encontrado"}

        if not data['customer_id']:
            return {"error": "Cliente e obrigatório para agendamento!!!"}, 404
        
        if not data['pet_id']:
            return {"error": "Pet e obrigatório para agendamento!!!"}, 404
        
        if not data['service_id']:
            return {"error": "Serviço e obrigatório para agendamento!!!"}, 404
        
        if not data['user_id']:
            return {"error": "Usuário e obrigatório para agendamento!!!"}, 404

        appointment.customer_id = data['customer_id']
        appointment.pet_id = data['pet_id']
        appointment.service_id = data['service_id']
        appointment.user_id = data['user_id']
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
