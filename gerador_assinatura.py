from PIL import Image, ImageDraw, ImageFont
import io
import os

# CONFIGURAÇÕES E CONSTANTES (Organização)
DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(DIRETORIO_BASE, 'static')
IMG_ASS_PADRAO = os.path.join(STATIC, 'assinatura_padrao_ses.png') # Junta o diretorio base com a pasta static e o nome do arquivo
FONTES = {
    'padrao': os.path.join(STATIC, 'arial.ttf'),
    'negrito': os.path.join(STATIC, 'ariblk.ttf'),
    'semicond': os.path.join(STATIC,'arialnb.ttf')
}

FONTES_PIL = {
    'nome': ImageFont.truetype(FONTES['negrito'], 24),
    'padraoGG': ImageFont.truetype(FONTES['padrao'], 24),
    'padraoG': ImageFont.truetype(FONTES['padrao'], 22),
    'orgao': ImageFont.truetype(FONTES['semicond'], 17),
}

TAMANHO_FINAL = (500, 241)
COORDS = {
    'nome': (55, 78),
    'cargo': (55, 134),
    'orgao': (56, 168),
    'telefone_fixo': (90, 286),
    'email': (90, 325),
    'endereco': (90, 370)
}

CORES = {
    'roxo': (131, 35, 112),
    'roxo_claro': (137, 71, 118),
    'laranja': (244, 148, 60)
}

# Função para gerar a assinatura com os dados recebidos
def gerar_assinatura(dados_usuario: dict) -> io.BytesIO:
    """ 
    Função para gerar a assinatura institucional da SES-MG com os dados do usuário.
    Usa o template de imagem padrão e preenche com os dados fornecidos.
    Parâmetros:
    dados_usuario (dict): Dicionário contendo os dados do usuário, como nome, cargo, órgão, telefone_fixo, email e andar.
    parametros pré-definidos e estaticos: coordenadas, cores e fontes(declarados como const no inicio do código).
    Retorna: buffer_memoria com a imagem gerada em formato PNG como um objeto BytesIO em memória, sem salvar no disco.
    """
    endereco = f'Cidade Administrativa, Prédio Minas, {dados_usuario['andar']} andar'

    try:
        img = Image.open(IMG_ASS_PADRAO).convert("RGBA") # Abre o template da imagem
        desenho = ImageDraw.Draw(img) # Criando camada de desenho sobre a imagem
        # Desenhando sobre a img com os dados do user, usando os parametros estaticos armazenados em dicts 
        desenho.text((COORDS['nome']), dados_usuario.get('nome', ''), font=FONTES_PIL['nome'], fill=CORES['roxo'])
        desenho.text((COORDS['cargo']), dados_usuario.get('cargo', ''), font=FONTES_PIL['padraoGG'], fill=CORES['roxo'])
        desenho.text((COORDS['orgao']), dados_usuario.get('orgao', ''), font=FONTES_PIL['orgao'], fill=CORES['laranja'])
        desenho.text((COORDS['telefone_fixo']), dados_usuario.get('telefone_fixo', ''), font=FONTES_PIL['padraoG'], fill=CORES['roxo'])
        desenho.text((COORDS['email']), dados_usuario.get('email', ''), font=FONTES_PIL['padraoG'], fill=CORES['roxo_claro'])
        desenho.text((COORDS['endereco']), endereco, font=FONTES_PIL['padraoG'], fill=CORES['roxo_claro'])

        img_redimensionada = img.resize(TAMANHO_FINAL, Image.Resampling.LANCZOS)

        buffer_memoria = io.BytesIO() # salvando o arquivo em memoria do servidor ao inves do disco
        img_redimensionada.save(buffer_memoria, format='PNG') # Salva a imagem redimensionada no buffer
        buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        return buffer_memoria # Retorna o buffer com a imagem gerada

    except FileNotFoundError:
        raise Exception("Erro interno. Arquivo de imagem não ou do template da assinatura não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado durante a geraçãoda imagem: {e}")