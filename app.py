from flask import Flask, request, jsonify, send_file
from validacao_dados import validar_dados
from normalizacao import normallizar_dados
from gerador_assinatura import gerar_assinatura

app = Flask(__name__)

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

    # Só executa os codigos abaxio se os dados forem válidos    
    # Chamando função para manipular dos dados recebidos (lowercase, upper, capitalize)
    normallizar_dados(dados_usuario)
    
    try:
        # Chamando a função para gerar a assinatura com os dados recebidos  
        imagem_gerada = gerar_assinatura(dados_usuario)
        # Retornando a imagem gerada para o usuário
        return send_file(
            imagem_gerada,
            mimetype='image/png',
            as_attachment=True,
            download_name=f"assinatura_{dados_usuario['nome'].replace(' ', '_')}.png"
        )

    except Exception as e:
        return jsonify({"error": f"Erro ao gerar a assinatura: {e}"}), 500

# Roda a aplicação em modo de depuração para facilitar o desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)