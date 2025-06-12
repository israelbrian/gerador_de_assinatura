from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

# Rota principal 
@app.route('/gerar_assinatura')
def gerar_assinatura():
     # Dados para a assinatura (teste)
    nome = "Israel Brian Pimenta Gonçalves Araújo"
    cargo = "Estagiario"
    secretaria = "Secretaria de estado de saude"
    orgao = "Assessoria de tecnologia da informação"
    telefone_fixo = "(31) 3277-0000"
    telefone_celular = "(31) 99999-9999"  # Este é opcional
    email = "nome.servidor@email.gov.br"
    endereco = "Av. Afonso Pena, 1212"
    andar = "10º andar"

    cord_nome = (55, 69)
    cord_cargo = (55, 108)
    cord_secretaria = (57, 148)

    # try:
        # Abre o template da imagem
    img = Image.open('/assinatura_padrao_ses.png').convert("RGBA")
    largura, altura = img.size

    # Carregando as fontes
    caminho_fonte = r"C:\Windows\Fonts\Calibri.TTF"
    font = ImageFont.truetype(caminho_fonte, 11)
    cor_texto = (0, 0, 0)  
    # Criando camada de desenho sobre a imagem
    desenho = ImageDraw.Draw(img)

    # Adicionando os textos na imagem
    # O formato é: desenho.text((coordenada_x, coordenada_y), texto, fill=cor, font=fonte)
    desenho.text((cord_nome), nome, font=font, fill=cor_texto)
    desenho.text((cord_cargo), cargo, font=font, fill=cor_texto)
    desenho.text((cord_secretaria), secretaria, font=font, fill=cor_texto)
    
    img.save(f'{nome}.png')
    img.show()

    