from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

# Rota principal 
@app.route('/')
def gerar_assinatura():
     # Dados para a assinatura (teste)
    nome = "Israel Brian Pimenta Gonçalves Araújo"
    # cargo = "Técnico em Informática - MGS"
    cargo = "Estagiario"
    orgao = "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO" 
    telefone_fixo = "(31) 3916 0031"
    # telefone_celular = "(31) 99999-9999"  # Este é opcional
    email = "israel.goncalves@saude.mg.gov.br"
    andar = "12º"
    endereco = f'Cidade Administrativa, Prédio Minas,{andar} andar'

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
        largura, altura = img.size

        # Carregando as fontes
        # Adicionar o os.path.join no caminho das fontes
        caminho_fonte = "static/arial.ttf" 
        caminho_fonte_negrito1 = "static/ariblk.ttf"
        # caminho_fonte_negrito2 = "static/arialbd.ttf"
        caminho_fonte_nb = "static/arialnb.ttf"
        # CRIAR PADRÃO PRO NOME - NEGRITO - 16 - ROXO
        fontNome = ImageFont.truetype(caminho_fonte_negrito1, 22)
        # CRIAR PADRÃO CARGO - NORMAL - 16 - ROXO
        fontPadraoGG = ImageFont.truetype(caminho_fonte, 22)
        fontPadraoG = ImageFont.truetype(caminho_fonte, 20)
        # CRIAR PADRÃO ORGAO - 12 - AMARELO - SEMPRE MAIUSCULO
        fontOrgao = ImageFont.truetype(caminho_fonte_nb, 17)
        texto_roxo = (131,35,112)  
        texto_roxo_claro = (137,71,118)  
        texto_laranja = (244,148,60)  
        # Criando camada de desenho sobre a imagem\
        desenho = ImageDraw.Draw(img)

        # Adicionando os textos na imagem
        # O formato é: desenho.text((coordenada_x, coordenada_y), texto, fill=cor, font=fonte)
        desenho.text((cord_nome), nome, font=fontNome, fill=texto_roxo)
        desenho.text((cord_cargo), cargo, font=fontPadraoGG, fill=texto_roxo)
        desenho.text((cord_orgao), orgao, font=fontOrgao, fill=texto_laranja)
        desenho.text((cord_tel_fixo), telefone_fixo, font=fontPadraoG, fill=texto_roxo)
        desenho.text((cord_email), email, font=fontPadraoG, fill=texto_roxo_claro)
        desenho.text((cord_end), endereco, font=fontPadraoG, fill=texto_roxo_claro)

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