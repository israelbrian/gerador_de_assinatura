# Manipulação dos dados recebidos (lowercase, upper, capitalize)
def normallizar_dados(dados_usuario):
    for chave, valor in dados_usuario.items():
        if isinstance(valor, str):
            if chave == 'nome' or chave == 'cargo':
                dados_usuario[chave] = valor.title().replace('De','de').replace('Da','da').replace('Das','das').replace('Do','do').replace('Dos','dos')  
            elif chave == 'orgao':
                dados_usuario[chave] = valor.upper().replace('De','de').replace('Em','em')     
            else:
                dados_usuario[chave] = valor.lower()
        