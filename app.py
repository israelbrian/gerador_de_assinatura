from flask import Flask, send_file, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

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
            return False, f"O valor para o campo '{chave}' não foi preenchido ou é inválido!"
    
    # Todos os campos foram validados com sucesso
    return True, "Dados validados com sucesso."

# Rota principal 
@app.route('/', methods=['POST'])
def gerar_assinatura():
    # RECEBENDO DADOS DO USUÁRIO VIA POST 
    try:        
        dados_usuario = request.get_json()
        if dados_usuario is None:
            return jsonify({"error": "Nenhum dado recebido"}), 400

        # Função de validação de dados 
        is_valid, mensagem_erro = validar_dados(dados_usuario)
        if not is_valid:
            return jsonify({"erro": mensagem_erro}), 400

    except Exception as e:
        return jsonify({"error": f"Erro ao processar os dados: {e}"}), 400
    
    # Após passar pela verificação dos dados -> Executa...
    # Manipulação dos dados recebidos (lowercase, upper, capitalize)

    for chave, valor in dados_usuario.items():
        if isinstance(valor, str):
            if chave == 'nome' or chave == 'cargo':
                dados_usuario[chave] = valor.title()  # Capitaliza o nome
            elif chave == 'orgao':
                dados_usuario[chave] = valor.upper()            
            else:
                dados_usuario[chave] = valor.lower()
    return jsonify({"message": "Dados recebidos e validados com sucesso", "dados": dados_usuario}), 200
    
    
     # Dados para a assinatura (teste)
    # nome = data_user['nome']  # Exemplo
    # cargo = "Técnico em Informática - MGS"
    # cargo = "Estagiario"
    # orgao = "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO" 
    # telefone_fixo = "(31) 3916 0031"
    # telefone_celular = "(31) 99999-9999"  # Este é opcional
    # email = "israel.goncalves@saude.mg.gov.br"
    # andar = "12º"
    # endereco = f'Cidade Administrativa, Prédio Minas,{andar} andar'

    # cord_nome = (55, 78)
    # cord_cargo = (55, 134)
    # cord_orgao = (56, 168)
    # cord_tel_fixo = (90, 286)
    # # cord_tel_cel = (90, 290)
    # cord_email = (90, 325)
    # cord_end = (90, 370)

    # try:
    #     # Abre o template da imagem
    #     img = Image.open('static/assinatura_padrao_ses.png').convert("RGBA")
    #     tamanho_final = 500, 241 # Tamanho que a imagem será salva
        # Carregando as fontes
        # Adicionar o os.path.join no caminho das fontes
        # caminho_fonte = "static/arial.ttf" 
        # caminho_fonte_negrito1 = "static/ariblk.ttf"
        # caminho_fonte_negrito2 = "static/arialbd.ttf"
        # caminho_fonte_nb = "static/arialnb.ttf"
        # CRIAR PADRÃO PRO NOME - NEGRITO - 16 - ROXO
        # fontNome = ImageFont.truetype(caminho_fonte_negrito1, 22)
        # CRIAR PADRÃO CARGO - NORMAL - 16 - ROXO
        # fontPadraoGG = ImageFont.truetype(caminho_fonte, 22)
        # fontPadraoG = ImageFont.truetype(caminho_fonte, 20)
        # CRIAR PADRÃO ORGAO - 12 - AMARELO - SEMPRE MAIUSCULO
        # fontOrgao = ImageFont.truetype(caminho_fonte_nb, 17)
        # texto_roxo = (131,35,112)  
        # texto_roxo_claro = (137,71,118)  
        # texto_laranja = (244,148,60)  
        # Criando camada de desenho sobre a imagem
        # desenho = ImageDraw.Draw(img)

        # Adicionando os textos na imagem
        # O formato é: desenho.text((coordenada_x, coordenada_y), texto, fill=cor, font=fonte)
        # desenho.text((cord_nome), nome, font=fontNome, fill=texto_roxo)
        # desenho.text((cord_cargo), cargo, font=fontPadraoGG, fill=texto_roxo)
        # desenho.text((cord_orgao), orgao, font=fontOrgao, fill=texto_laranja)
        # desenho.text((cord_tel_fixo), telefone_fixo, font=fontPadraoG, fill=texto_roxo)
        # desenho.text((cord_email), email, font=fontPadraoG, fill=texto_roxo_claro)
        # desenho.text((cord_end), endereco, font=fontPadraoG, fill=texto_roxo_claro)

        #  algoritmo de reamostragem usando o método reside() (resampling) (LANCZOS)
        # img_redimensionada = img.resize(tamanho_final, Image.Resampling.LANCZOS)

        # # Salva a imagem gerada em memória
        # # io.BytesIO serve salvar o arquivo em memoria do servidor ao inves do disco.
        # buffer_memoria = io.BytesIO()
        # img_redimensionada.save(buffer_memoria, format='PNG')
        # buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        # salvando o arquivo com o nome do usuário ---
    #     return send_file(
    #         buffer_memoria,
    #         mimetype='image/png',
    #         # as_attachment=True,
    #         # download_name=f'{nome}.png'
    #     )

    # except FileNotFoundError:
    #     return "Erro: 'template_assinatura.png' ou 'Calibri.ttf' não encontrado no diretório.", 404
    # except Exception as e:
    #     return f"Ocorreu um erro inesperado: {e}", 500

# Roda a aplicação em modo de depuração para facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)