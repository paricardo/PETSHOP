import re
from datetime import datetime


""" VALIDAÇÃO DE DATA """
date_now = datetime.now().replace(second=0, microsecond=0)


""" VALIDAÇÃO DE EMAIL """
def validate_email(email: str) -> str | bool:
    """
    Valida formato básico de email.
    """

    if not email:
        return True
    
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))


""" VALIDAÇÃO DE TELEFONE """
def format_phone(phone: str) -> tuple[str, bool]:
    numbers = ''.join(filter(str.isdigit, phone))

    if len(numbers) != 11:
        return "Telefone deve conter 11 dígitos", False

    formatted_phone = f"({numbers[:2]}) {numbers[2:7]}-{numbers[7:]}"

    return formatted_phone, True