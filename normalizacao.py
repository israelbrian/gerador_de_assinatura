# Manipulação dos dados recebidos (lowercase, upper, capitalize)
def normallizar_dados(dados_usuario):
    for chave, valor in dados_usuario.items():
        if isinstance(valor, str):
            # if chave == 'nome':
            if chave == 'nome' or chave == 'cargo':
                # if 'de' in chave:
                # Capitalizando os campos / Exceto os complementos (da, das, de, do, dos)
                dados_usuario[chave] = valor.title().replace('De','de').replace('Da','da').replace('Das','das').replace('Do','do').replace('Dos','dos')  
            elif chave == 'orgao':
                dados_usuario[chave] = valor.upper()            
            else:
                dados_usuario[chave] = valor.lower()