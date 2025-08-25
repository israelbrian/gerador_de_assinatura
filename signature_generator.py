from PIL import Image, ImageDraw, ImageFont
import io
import os

DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(DIRETORIO_BASE, 'static')
SIGNATURE_DEFAULT = os.path.join(STATIC, 'images/new_default_signature_ses.png')
FINAL_SIZE = (500, 241)
MAX_SIZE = 37

FONTS = {
    'default': os.path.join(STATIC, 'fonts/arial.ttf'),
    'negrito': os.path.join(STATIC, 'fonts/ariblk.ttf'),
    'semicond': os.path.join(STATIC,'fonts/arialnb.TTF')
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

def signatureGenerator(normalizedUserData: dict) -> io.BytesIO:
    adress = f"Cidade Administrativa, Prédio Minas, {normalizedUserData.get('floor', '')}° andar"

    try:

        FONTS_PIL = {
        'name': ImageFont.truetype(FONTS['negrito'], 24),
        'nameSmall': ImageFont.truetype(FONTS['negrito'], 22),
        'defaultGG': ImageFont.truetype(FONTS['default'], 24),
        'defaultG': ImageFont.truetype(FONTS['default'], 22),
        'department': ImageFont.truetype(FONTS['semicond'], 17)
        }
        img = Image.open(SIGNATURE_DEFAULT).convert("RGBA")
        desenho = ImageDraw.Draw(img)

        if len(normalizedUserData.get('fullName', '')) > MAX_SIZE:
            desenho.text((COORDS['name']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['nameSmall'], fill=COLORS['purple'])
        else:       
            desenho.text((COORDS['name']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['name'], fill=COLORS['purple'])
        desenho.text((COORDS['jobTitle']), normalizedUserData.get('jobTitle', ''), font=FONTS_PIL['defaultGG'], fill=COLORS['purple'])
        desenho.text((COORDS['department']), normalizedUserData.get('department', ''), font=FONTS_PIL['department'], fill=COLORS['orange'])
        desenho.text((COORDS['phoneNumber']), normalizedUserData.get('phoneNumber', ''), font=FONTS_PIL['defaultG'], fill=COLORS['purple'])
        desenho.text((COORDS['email']), normalizedUserData.get('email', ''), font=FONTS_PIL['defaultG'], fill=COLORS['purpleLight'])
        desenho.text((COORDS['adress']), adress, font=FONTS_PIL['defaultG'], fill=COLORS['purpleLight'])

        imgResized = img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)

        bufferMemory = io.BytesIO()
        imgResized.save(bufferMemory, format='PNG')
        bufferMemory.seek(0)

        return bufferMemory

    except FileNotFoundError:
        raise Exception("Erro interno. Arquivo de imagem ou do template da assinatura não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado durante a geraçãoda imagem: {e}")