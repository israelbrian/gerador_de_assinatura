from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

# Rota principal 
@app.route('/')
def gerar_assinatura():
     # Dados para a assinatura (teste)
    nome = "Rogerio el salvador el shaday"
    cargo = "Técnico em informática - MGS"
    secretaria = "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO" # Desnecessario, temporario pra teste
    orgao = "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO" # Desnecessario, temporario pra teste
    telefone_fixo = "(31) 3277-0000"
    telefone_celular = "(31) 99999-9999"  # Este é opcional
    email = "nome.servidor@email.gov.br"
    endereco = "Av. Afonso Pena, 1212"
    andar = "10º andar"

    cord_nome = (50, 76)
    cord_cargo = (52, 115)
    cord_secretaria = (52, 145)

    try:
        # Abre o template da imagem
        img = Image.open('static/assinatura_padrao_ses.png').convert("RGBA")
        largura, altura = img.size

        # Carregando as fontes
        # Adicionar o os.path.join no caminho das fontes
        caminho_fonte = "static/calibri.ttf" 
        caminho_fonte_negrito = "static/calibrib.ttf"
        # CRIAR PADRÃO PRO NOME - NEGRITO - 16 - ROXO
        fontNome = ImageFont.truetype(caminho_fonte_negrito, 22)
        # CRIAR PADRÃO CARGO - NORMAL - 16 - ROXO
        fontCargo = ImageFont.truetype(caminho_fonte, 20)
        # CRIAR PADRÃO ORGAO - 12 - AMARELO - SEMPRE MAIUSCULO
        fontOrgao = ImageFont.truetype(caminho_fonte_negrito, 18)
        texto_roxo = (100, 0, 100)  
        texto_laranja = (246, 120, 40)  
        # Criando camada de desenho sobre a imagem\
        desenho = ImageDraw.Draw(img)

        # Adicionando os textos na imagem
        # O formato é: desenho.text((coordenada_x, coordenada_y), texto, fill=cor, font=fonte)
        desenho.text((cord_nome), nome, font=fontNome, fill=texto_roxo)
        desenho.text((cord_cargo), cargo, font=fontCargo, fill=texto_roxo)
        desenho.text((cord_secretaria), secretaria, font=fontOrgao, fill=texto_laranja)

        # Salva a imagem gerada em memória
        # Usamos io.BytesIO para evitar salvar o arquivo no disco do servidor.
        buffer_memoria = io.BytesIO()
        img.save(buffer_memoria, format='PNG')
        buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        # --- 6. Envia o arquivo para o usuário ---
        return send_file(
            buffer_memoria,
            mimetype='image/png',
            as_attachment=True,
            download_name=f'{nome}.png' # Nome do arquivo para download
        )

    except FileNotFoundError:
        return "Erro: 'template_assinatura.png' ou 'Calibri.ttf' não encontrado no diretório.", 404
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}", 500

# Roda a aplicação em modo de depuração para facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)

    