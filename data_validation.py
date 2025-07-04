# Função para validar os dados do usuário
def validate_data(dados_usuario):
    chaves_obrigatorias = ['nome', 'cargo', 'orgao', 'telefone_fixo', 'email', 'andar']
    for chave in chaves_obrigatorias:
        if chave not in dados_usuario:
            return False, f"Campo obrigatório '{chave}' não encontrada nos dados do usuário."
        valor = dados_usuario[chave]
        if not valor or not str(valor).strip():
            return False, f"O valor para o campo '{chave}' nao foi preenchido ou é invalido!"
        
    return True, "Dados validados com sucesso."