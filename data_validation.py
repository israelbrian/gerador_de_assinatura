# Função para validar os dados do usuário
def validate_data(userData):
    mandatoryKeys = ['fullName', 'jobTitle', 'department', 'phoneNumber', 'email', 'floor']
    for key in mandatoryKeys:
        if key not in userData:
            return False, f"Campo obrigatório '{key}' não encontrada nos dados do usuário."
        value = userData[key]
        if not value or not str(value).strip():
            return False, f"O valor para o campo '{key}' nao foi preenchido ou é invalido!"
        
    return True, "Dados validados com sucesso."