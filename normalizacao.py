# Manipulação dos dados recebidos (lowercase, upper, capitalize)
def normallizar_dados(dados_usuario):
    for chave, valor in dados_usuario.items():
        if isinstance(valor, str):
            if chave == 'nome' or chave == 'cargo':
                dados_usuario[chave] = valor.title()  # Capitaliza o nome
            elif chave == 'orgao':
                dados_usuario[chave] = valor.upper()            
            else:
                dados_usuario[chave] = valor.lower()