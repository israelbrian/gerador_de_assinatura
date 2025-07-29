import re

def validateData(userData):
    mandatoryKeys = ['fullName', 'jobTitle', 'department', 'phoneNumber', 'email', 'floor']
    
    patterns = {
        'fullName': r'^[A-Za-zÀ-ú\s]{5,}$',
        'jobTitle': r'^.{5,}$',
        'phoneNumber': r'^\d{10}$', 
        'email': r'^[a-zA-Z.]+@saude\.mg\.gov\.br$',
        'department': r'^.{5,}$',
        'floor': r'^.{2}$'
    }

    for key in mandatoryKeys:
        if key not in userData or not str(userData.get(key, '')).strip():
            return False, f"O campo obrigatório '{key}' não foi enviado ou está vazio."
    
    for key, pattern in patterns.items():
        value = str(userData.get(key, ''))

        if key == 'phoneNumber':
            value = re.sub(r'\D', '', value)

        if not re.fullmatch(pattern, value):
            return False, f"O formato do dado para o campo '{key}' é inválido."
            
    return True, "Dados validados com sucesso."

# def validateData(userData):
#     mandatoryKeys = ['fullName', 'jobTitle', 'department', 'phoneNumber', 'email', 'floor']
#     for key in mandatoryKeys:
#         if key not in userData:
#             return False, f"Campo obrigatório '{key}' não encontrada nos dados do usuário."
#         value = userData[key]
#         if not value or not str(value).strip():
#             return False, f"O valor para o campo '{key}' nao foi preenchido ou é invalido!"
        
#     return True, "Dados validados com sucesso."