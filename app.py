from flask import Flask, send_file
from PIL import Image, ImageFont, ImageDraw
import io

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota principal que irá gerar a assinatura
@app.route('/gerar_assinatura')
def gerar_assinatura():
    """
    Gera uma imagem de assinatura com dados fixos e a retorna para download.
    """
    # --- 1. Dados para a assinatura (atualmente como variáveis locais) ---
    nome = "Nome Completo do Servidor"
    cargo = "Cargo do Servidor"
    secretaria = "Secretaria Municipal de Exemplo"
    orgao = "Departamento ou Setor"
    telefone_fixo = "(31) 3277-0000"
    telefone_celular = "(31) 99999-9999"  # Este é opcional
    email = "nome.servidor@email.gov.br"
    endereco = "Av. Afonso Pena, 1212"
    andar = "10º andar"

    try:
        # --- 2. Abre a imagem de template ---
        # Certifique-se de que o nome do arquivo corresponde ao seu.
        img = Image.open("template_assinatura.png").convert("RGBA")
        largura, altura = img.size

        # Cria uma camada de desenho sobre a imagem
        desenho = ImageDraw.Draw(img)

        # --- 3. Carrega as fontes ---
        # O número representa o tamanho da fonte. Ajuste conforme necessário.
        fonte_nome = ImageFont.truetype("Arial.ttf", 32)
        fonte_cargo = ImageFont.truetype("Arial.ttf", 26)
        fonte_info = ImageFont.truetype("Arial.ttf", 24)
        cor_texto = (0, 0, 0)  # Cor do texto em RGB (preto)

        # --- 4. Adiciona os textos na imagem ---
        # O formato é: desenho.text((coordenada_x, coordenada_y), texto, fill=cor, font=fonte)
        # Você PRECISARÁ ajustar as coordenadas (x, y) para a sua imagem.
        desenho.text((250, 50), nome, fill=cor_texto, font=fonte_nome)
        desenho.text((250, 90), cargo, fill=cor_texto, font=fonte_cargo)
        desenho.text((250, 125), secretaria, fill=cor_texto, font=fonte_info)
        desenho.text((250, 155), orgao, fill=cor_texto, font=fonte_info)
        desenho.text((250, 200), f"Tel: {telefone_fixo}", fill=cor_texto, font=fonte_info)

        # Adiciona o celular apenas se a variável não estiver vazia
        if telefone_celular:
            desenho.text((250, 230), f"Cel: {telefone_celular}", fill=cor_texto, font=fonte_info)

        desenho.text((250, 260), email, fill=cor_texto, font=fonte_info)
        desenho.text((250, 290), f"{endereco} - {andar}", fill=cor_texto, font=fonte_info)

        # --- 5. Salva a imagem gerada em memória ---
        # Usamos io.BytesIO para evitar salvar o arquivo no disco do servidor.
        buffer_memoria = io.BytesIO()
        img.save(buffer_memoria, format='PNG')
        buffer_memoria.seek(0) # Volta ao início do "arquivo" em memória

        # --- 6. Envia o arquivo para o usuário ---
        return send_file(
            buffer_memoria,
            mimetype='image/png',
            as_attachment=True,
            download_name='minha_assinatura.png' # Nome do arquivo para download
        )

    except FileNotFoundError:
        return "Erro: 'template_assinatura.png' ou 'Arial.ttf' não encontrado no diretório.", 404
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}", 500

# Roda a aplicação em modo de depuração para facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)