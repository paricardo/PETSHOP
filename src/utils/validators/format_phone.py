""" VALIDAÇÃO DE TELEFONE """
def format_phone(phone: str) -> tuple[str, bool]:
    numbers = ''.join(filter(str.isdigit, phone))

    if len(numbers) != 11:
        return "Telefone deve conter 11 dígitos", False

    formatted_phone = f"({numbers[:2]}) {numbers[2:7]}-{numbers[7:]}"

    return formatted_phone, True