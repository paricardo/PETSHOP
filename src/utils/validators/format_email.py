import re

""" VALIDAÇÃO DE EMAIL """
def validate_email(email: str) -> str | bool:
    """
    Valida formato básico de email.
    """

    if not email:
        return True
    
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))