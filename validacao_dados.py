# Função para validar os dados do usuário
def validar_dados(dados_usuario):
    chaves_obrigatorias = ['nome', 'cargo', 'orgao', 'telefone_fixo', 'email', 'andar']
    # Verifica se todas as chaves obrigatórias estão presentes
    for chave in chaves_obrigatorias:
        if chave not in dados_usuario:
            return False, f"Campo obrigatório '{chave}' não encontrada nos dados do usuário."
        # Garantindo que os valores não sejam vazios
        valor = dados_usuario[chave]
        if not valor or not str(valor).strip():
            return False, f"O valor para o campo '{chave}' nao foi preenchido ou é invalido!"
        
    # Todos os campos foram validados com sucesso
    return True, "Dados validados com sucesso."