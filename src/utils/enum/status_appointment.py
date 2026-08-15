from enum import Enum

class StatusAppointment(Enum):
    FINISHED = 'finished'
    COMPLETED = 'completed'
    SCHEDULED = 'scheduled'
    IN_PROGRESS = 'in_progress'
    CANCELED = 'canceled'
    PAYMENT = 'payment'