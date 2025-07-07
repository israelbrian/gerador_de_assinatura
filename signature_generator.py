from PIL import Image, ImageDraw, ImageFont
import io
import os

DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(DIRETORIO_BASE, 'static')
SIGNATURE_DEFAULT = os.path.join(STATIC, 'default_signature_ses.PNG')
FINAL_SIZE = (500, 241)

FONTES = {
    'default': os.path.join(STATIC, 'arial.ttf'),
    'negrito': os.path.join(STATIC, 'ariblk.ttf'),
    'semicond': os.path.join(STATIC,'arialnb.TTF')
}

COORDS = {
    'name': (55, 78),
    'jobTitle': (55, 134),
    'department': (56, 168),
    'phoneNumber': (90, 286),
    'email': (90, 325),
    'adress': (90, 370)
}

COLORS = {
    'purple': (131, 35, 112),
    'purpleLight': (137, 71, 118),
    'orange': (244, 148, 60)
}

def signatureGenerator(userData: dict) -> io.BytesIO:
    """ 
    Função para gerar a assinatura institucional da SES-MG com os dados do usuário.
    Usa o template de imagem padrão e preenche com os dados fornecidos.
    Parâmetros:
    userData (dict): Dicionário contendo os dados do usuário, como name, jobTitle, órgão, phoneNumber, email e andar.
    Parametros pré-definidos e estaticos: coordenadas, COLORS e fontes(declarados como const no inicio do código).
    Retorno: bufferMemory com a imagem gerada em formato PNG como um objeto BytesIO em memória, sem salvar no disco.
    """
    adress = f"Cidade Administrativa, Prédio Minas, {userData.get('floor', '')} andar"

    try:

        FONTES_PIL = {
        'name': ImageFont.truetype(FONTES['negrito'], 24),
        'defaultGG': ImageFont.truetype(FONTES['default'], 24),
        'defaultG': ImageFont.truetype(FONTES['default'], 22),
        'department': ImageFont.truetype(FONTES['semicond'], 17)
        }
        img = Image.open(SIGNATURE_DEFAULT).convert("RGBA")
        desenho = ImageDraw.Draw(img)

        desenho.text((COORDS['name']), userData.get('fullName', ''), font=FONTES_PIL['name'], fill=COLORS['purple'])
        desenho.text((COORDS['jobTitle']), userData.get('jobTitle', ''), font=FONTES_PIL['defaultGG'], fill=COLORS['purple'])
        desenho.text((COORDS['department']), userData.get('department', ''), font=FONTES_PIL['department'], fill=COLORS['orange'])
        desenho.text((COORDS['phoneNumber']), userData.get('phoneNumber', ''), font=FONTES_PIL['defaultG'], fill=COLORS['purple'])
        desenho.text((COORDS['email']), userData.get('email', ''), font=FONTES_PIL['defaultG'], fill=COLORS['purpleLight'])
        desenho.text((COORDS['adress']), adress, font=FONTES_PIL['defaultG'], fill=COLORS['purpleLight'])

        imgResized = img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)

        bufferMemory = io.BytesIO()
        imgResized.save(bufferMemory, format='PNG')
        bufferMemory.seek(0)

        return bufferMemory

    except FileNotFoundError:
        raise Exception("Erro interno. Arquivo de imagem ou do template da assinatura não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado durante a geraçãoda imagem: {e}")