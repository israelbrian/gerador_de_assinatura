from PIL import Image, ImageDraw, ImageFont
import io
import os

DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(DIRETORIO_BASE, 'static')
SIGNATURE_DEFAULT = os.path.join(STATIC, 'images/new_default_signature_ses.png')
FINAL_SIZE = (500, 241)
MAX_SIZE_MEDIUM = 22
MAX_SIZE_LONG = 30

FONTS = {
    'default': os.path.join(STATIC, 'fonts/arial.ttf'),
    'negrito': os.path.join(STATIC, 'fonts/ariblk.ttf'),
    'negritoLow': os.path.join(STATIC, 'fonts/arialbd.ttf'),
    'semicond': os.path.join(STATIC,'fonts/arialnb.TTF')
}

COORDS = {
    'name': (53, 68),
    'nameSmall': (53, 80),
    'jobTitle': (53, 117),
    'department': (53, 160),
    'phoneNumber': (90, 285),
    'telephoneNumber': (216, 285),
    'email': (90, 325),
    'adress': (90, 368)
}

COLORS = {
    'purple': (131, 35, 112),
    'darkPurple': (122, 48, 100),
    'purpleLight': (137, 71, 118),
    'orange': (254, 159, 33),
    'orangeLight': (207, 163, 105)
}

def signatureGenerator(normalizedUserData: dict) -> io.BytesIO:
    try:

        FONTS_PIL = {
        'name': ImageFont.truetype(FONTS['negrito'], 40),
        'fontLarge': ImageFont.truetype(FONTS['negrito'], 28),
        'fontMedium': ImageFont.truetype(FONTS['negrito'], 20),
        'fontDefault': ImageFont.truetype(FONTS['negrito'], 18),
        'fontSmall': ImageFont.truetype(FONTS['negrito'], 16),
        'fontMoreSmall': ImageFont.truetype(FONTS['negrito'], 14),
        'fontMoreSmall2': ImageFont.truetype(FONTS['negrito'], 12),
        'department': ImageFont.truetype(FONTS['semicond'], 18),
        'info': ImageFont.truetype(FONTS['negritoLow'], 18),
        'infoBold': ImageFont.truetype(FONTS['semicond'], 22)
        }
        img = Image.open(SIGNATURE_DEFAULT).convert("RGBA")
        desenho = ImageDraw.Draw(img)
    
        if len(normalizedUserData.get('fullName', '')) > 58:
            desenho.text((COORDS['nameSmall']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['fontMoreSmall2'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('fullName', '')) > 49:
            desenho.text((COORDS['nameSmall']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['fontMoreSmall'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('fullName', '')) > 39:
            desenho.text((COORDS['nameSmall']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['fontSmall'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('fullName', '')) > 27:
            desenho.text((COORDS['name']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['fontMedium'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('fullName', '')) > 19:
            desenho.text((COORDS['name']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['fontLarge'], fill=COLORS['purple'])
        else:
            desenho.text((COORDS['name']), normalizedUserData.get('fullName', ''), font=FONTS_PIL['name'], fill=COLORS['purple'])
        
        if len(normalizedUserData.get('jobTitle', '')) > 59:
            desenho.text((COORDS['jobTitle']), normalizedUserData.get('jobTitle', ''), font=FONTS_PIL['fontMoreSmall2'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('jobTitle', '')) > 45:
            desenho.text((COORDS['jobTitle']), normalizedUserData.get('jobTitle', ''), font=FONTS_PIL['fontMoreSmall'], fill=COLORS['purple'])
        elif len(normalizedUserData.get('jobTitle', '')) > 35:
            desenho.text((COORDS['jobTitle']), normalizedUserData.get('jobTitle', ''), font=FONTS_PIL['fontDefault'], fill=COLORS['purple'])
        else:
            desenho.text((COORDS['jobTitle']), normalizedUserData.get('jobTitle', ''), font=FONTS_PIL['fontMedium'], fill=COLORS['purple'])
        desenho.text((COORDS['department']), normalizedUserData.get('department', ''), font=FONTS_PIL['department'], fill=COLORS['orange'])
        desenho.text((COORDS['phoneNumber']), normalizedUserData.get('phoneNumber', ''), font=FONTS_PIL['info'], fill=COLORS['darkPurple'])
        telephone_number = normalizedUserData.get('telephoneNumber')
        if telephone_number:
            desenho.text(COORDS['telephoneNumber'], f"/ {telephone_number}", font=FONTS_PIL['info'], fill=COLORS['darkPurple'])
        desenho.text((COORDS['email']), normalizedUserData.get('email', ''), font=FONTS_PIL['info'], fill=COLORS['darkPurple'])
        desenho.text((COORDS['adress']), normalizedUserData.get('adress', ''), font=FONTS_PIL['info'], fill=COLORS['darkPurple'])

        # desenho.text((COORDS['adress']), adress, font=FONTS_PIL['info'], fill=COLORS['darkPurple'])

        imgResized = img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)

        bufferMemory = io.BytesIO()
        imgResized.save(bufferMemory, format='PNG')
        bufferMemory.seek(0)

        return bufferMemory

    except FileNotFoundError:
        raise Exception("Erro interno. Arquivo de imagem ou do template da assinatura não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado durante a geraçãoda imagem: {e}")