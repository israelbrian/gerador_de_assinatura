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

# def gerar_assinatura(dados_usuario):
#     # Função para gerar a assinatura com os dados do usuário
#     for chave, valor in dados_usuario.items():
#         if isinstance(valor, str):


# Rota principal 
@app.route('/', methods=['POST'])
def receber_dados():
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
    
    # Logica para gerar a assinatura com os dados recebidos  

    endereco = f'Cidade Administrativa, Prédio Minas, {dados_usuario['andar']} andar'
    # return jsonify({"message": "Dados recebidos e validados com sucesso", "dados": dados_usuario}), 200
    
    cord_nome = (55, 78)
    cord_cargo = (55, 134)
    cord_orgao = (56, 168)
    cord_tel_fixo = (90, 286)
    # cord_tel_cel = (90, 290)
    cord_email = (90, 325)
    cord_end = (90, 370)

    try:
        # Abre o template da imagem
        img = Image.open('static/assinatura_padrao_ses.png').convert("RGBA")
        tamanho_final = 500, 241 # Tamanho que a imagem será salva
        # Carregando as fontes - LEMBRAR DE ADICONAR o os.path.join no caminho das fontes / imagem
        caminho_fonte = "static/arial.ttf" 
        caminho_fonte_negrito1 = "static/ariblk.ttf"
        caminho_fonte_negrito2 = "static/arialbd.ttf"
        caminho_fonte_nb = "static/arialnb.ttf"
        fontNome = ImageFont.truetype(caminho_fonte_negrito1, 22)
        fontPadraoGG = ImageFont.truetype(caminho_fonte, 22)
        fontPadraoG = ImageFont.truetype(caminho_fonte, 20)
        fontOrgao = ImageFont.truetype(caminho_fonte_nb, 17)
        texto_roxo = (131,35,112)  
        texto_roxo_claro = (137,71,118)  
        texto_laranja = (244,148,60)  
        # Criando camada de desenho sobre a imagem
        desenho = ImageDraw.Draw(img)

        # Adicionando os textos na imagem
        desenho.text((cord_nome), dados_usuario['nome'], font=fontNome, fill=texto_roxo)
        desenho.text((cord_cargo), dados_usuario['cargo'], font=fontPadraoGG, fill=texto_roxo)
        desenho.text((cord_orgao), dados_usuario['orgao'], font=fontOrgao, fill=texto_laranja)
        desenho.text((cord_tel_fixo), dados_usuario['telefone_fixo'], font=fontPadraoG, fill=texto_roxo)
        desenho.text((cord_email), dados_usuario['email'], font=fontPadraoG, fill=texto_roxo_claro)
        desenho.text((cord_end), endereco, font=fontPadraoG, fill=texto_roxo_claro)

        # Algoritmo de reamostragem usando o método reside() (resampling) (LANCZOS)
        img_redimensionada = img.resize(tamanho_final, Image.Resampling.LANCZOS)

        buffer_memoria = io.BytesIO() # salvando o arquivo em memoria do servidor ao inves do disco
        img_redimensionada.save(buffer_memoria, format='PNG') # Salva a imagem redimensionada no buffer
        buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        # Retornando o arquivo com o nome do usuário
        return send_file(
            buffer_memoria,
            mimetype='image/png',
            as_attachment=True,
            download_name=f'{dados_usuario['nome']}.png'
        )

    except FileNotFoundError:
        return "Erro: 'template_assinatura.png' ou 'Calibri.ttf' não encontrado no diretório.", 404
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}", 500

# Roda a aplicação em modo de depuração para facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)