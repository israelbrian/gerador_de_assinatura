# Manipulação dos dados recebidos (lowercase, upper, capitalize)
def normallize_data(dados_usuario):
    for chave, valor in dados_usuario.items():
        if isinstance(valor, str):
            if chave == 'nome' or chave == 'cargo':
                dados_usuario[chave] = valor.title().replace('De','de').replace('Da','da').replace('Das','das').replace('Do','do').replace('Dos','dos')  
            elif chave == 'orgao':
                dados_usuario[chave] = valor.upper().replace('De','de').replace('Em','em')  
            elif chave == 'telefone_fixo':
                if len(valor) == 10:
                    dados_usuario[chave] = valor[0:2] + ' ' + valor[2:6] + '-' + valor[6:10]
            else:
                dados_usuario[chave] = valor.lower()
        