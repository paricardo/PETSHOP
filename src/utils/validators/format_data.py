from datetime import datetime

def formatar_data_sp(data_str):
    """
    Recebe uma data em string no formato ISO (aaaa-mm-dd), 
    como vem de um input HTML type="date", e retorna no 
    formato brasileiro: dd/mm/aaaa
    """
    data = datetime.strptime(data_str, "%Y-%m-%d").date()
    return data.strftime("%d/%m/%Y")