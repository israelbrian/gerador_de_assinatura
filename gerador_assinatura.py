from PIL import Image, ImageDraw, ImageFont
import io

# Função para gerar a assinatura com os dados recebidos
def gerar_assinatura(dados_usuario):
    endereco = f'Cidade Administrativa, Prédio Minas, {dados_usuario['andar']} andar'
    cord_nome = (55, 78)
    cord_cargo = (55, 134)
    cord_orgao = (56, 168)
    cord_tel_fixo = (90, 286)
    # cord_tel_cel = (90, 290) implementar futuramente
    cord_email = (90, 325)
    cord_end = (90, 370)

    try:
        # Abre o template da imagem
        img = Image.open('static/assinatura_padrao_ses.png').convert("RGBA")
        tamanho_final = 500, 241 # Tamanho que a imagem será salva
        # Carregando as fontes - LEMBRAR DE ADICONAR o os.path.join no caminho das fontes / imagem
        fontes = {
            'font_padrao': 'static/arial.ttf',
            'font_negrito': 'static/ariblk.ttf',
            'fonte_semicond': 'static/arialnb.ttf'  # Fonte semicondensada negrito - usada em orgao
        }

        fonteNome = ImageFont.truetype(fontes['font_negrito'], 22)
        fontePadraoGG = ImageFont.truetype(fontes['font_padrao'], 22)
        fontePadraoG = ImageFont.truetype(fontes['font_padrao'], 20)
        fonteOrgao = ImageFont.truetype(fontes['fonte_semicond'], 17)
        texto_roxo = (131,35,112)  
        texto_roxo_claro = (137,71,118)  
        texto_laranja = (244,148,60)  
        desenho = ImageDraw.Draw(img) # Criando camada de desenho sobre a imagem

        # Adicionando os textos na imagem
        desenho.text((cord_nome), dados_usuario['nome'], font=fonteNome, fill=texto_roxo)
        desenho.text((cord_cargo), dados_usuario['cargo'], font=fontePadraoGG, fill=texto_roxo)
        desenho.text((cord_orgao), dados_usuario['orgao'], font=fonteOrgao, fill=texto_laranja)
        desenho.text((cord_tel_fixo), dados_usuario['telefone_fixo'], font=fontePadraoG, fill=texto_roxo)
        desenho.text((cord_email), dados_usuario['email'], font=fontePadraoG, fill=texto_roxo_claro)
        desenho.text((cord_end), endereco, font=fontePadraoG, fill=texto_roxo_claro)
        # desenho.text((cord_nome), dados_usuario.get('nome', ''), font=fonteNome, fill=texto_roxo)
        # desenho.text((cord_cargo), dados_usuario.get('cargo', ''), font=fontePadraoGG, fill=texto_roxo)
        # desenho.text((cord_orgao), dados_usuario.get('orgao', ''), font=fonteOrgao, fill=texto_laranja)
        # desenho.text((cord_tel_fixo), dados_usuario.get('telefone_fixo', ''), font=fontePadraoG, fill=texto_roxo)
        # desenho.text((cord_email), dados_usuario.get('email', ''), font=fontePadraoG, fill=texto_roxo_claro)
        # desenho.text((cord_end), endereco, font=fontePadraoG, fill=texto_roxo_claro)

        # Algoritmo de reamostragem usando o método reside() (resampling) (LANCZOS)
        img_redimensionada = img.resize(tamanho_final, Image.Resampling.LANCZOS)

        buffer_memoria = io.BytesIO() # salvando o arquivo em memoria do servidor ao inves do disco
        img_redimensionada.save(buffer_memoria, format='PNG') # Salva a imagem redimensionada no buffer
        buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        # Retorna o buffer com a imagem gerada
        return buffer_memoria

    except FileNotFoundError:
        raise Exception("Erro interno. Arquivo de imagem não ou do template da assinatura não foi encontrado.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado durante a geraçãoda imagem: {e}")