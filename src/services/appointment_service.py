from src.models.appointment import Appointment
from src.models.user import User
from src.models.customer import Customer
from src.models.pet import Pet
from src.models.package import Package
from src.utils.validators.format_data import formatar_data_sp
from src.utils.enum.status_appointment import StatusAppointment


class AppointmentService:

    def search(self, query: str):
        appointments = Appointment.select().where(
            (Appointment.scheduled_at.contains(query))
        )

        return appointments


    # Este serviço é responsável por concluir uma tarefa em aberto
    def completed_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.COMPLETED.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }


    # Este serviço é responsável por finalizar uma tarefa em aberto
    def finished_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.FINISHED.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }


    # Este serviço é responsável por inicializar uma tarefa
    def in_progress_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.IN_PROGRESS.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }

    # Este serviço é responsável por cancelar uma tarefa em aberto
    def canceled_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.CANCELED.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }

    # Este serviço é responsável por agendar uma tarefa 
    def scheduled_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.SCHEDULED.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }


    # Este serviço é responsável por aguardar pagamento de uma tarefa em aberto
    def awaiting_payment_appointments(self, appointment_id: int):
        appointment = Appointment.get_or_none(
            Appointment.id == appointment_id
        )

        if not appointment:
            return {"message": "Agendamento não encontrado", "status": False}
        
        appointment.status = StatusAppointment.PAYMENT.value
        appointment.save()

        return {
            "message": "Agendamento concluído com sucesso",
            "status": True
        }
    
    

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
            "package_id": appointment_id.package_id_id,
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

        scheduled_at = formatar_data_sp(data['scheduled_at'])

        status = StatusAppointment(data['status']).value
        

        Appointment.create(
            customer_id = customer,
            pet_id = pet,
            package_id = package,
            user_id = user,
            final_price = data['final_price'],
            scheduled_at = scheduled_at,
            status = status,
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

        scheduled_at = formatar_data_sp(data['scheduled_at'])

        appointment.customer_id = customer
        appointment.pet_id = pet
        appointment.package_id_id = package
        appointment.user_id = user
        appointment.scheduled_at = scheduled_at
        appointment.status = StatusAppointment(data['status']).value
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
