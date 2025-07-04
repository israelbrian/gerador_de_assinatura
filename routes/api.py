from flask import Blueprint, request, jsonify, send_file, current_app

from data_validation import validate_data
from normalize import normallize_data
from signature_generator import generator_signature

# 1. Cria o Blueprint para a API.
api_route = Blueprint('api_route', __name__)

# 2. Define a rota da API usando o Blueprint.
@api_route.route('/api', methods=['POST'])
def receber_dados():
    """Recebe os dados do formulário, valida, normaliza e gera a assinatura."""
    try:
        dados_usuario = request.get_json()
        if dados_usuario is None:
            return jsonify({"error": "Nenhum dado recebido"}), 400

        is_valid, mensagem_erro = validate_data(dados_usuario)
        if not is_valid:
            return jsonify({"erro": mensagem_erro}), 400

    except Exception as e:
        return jsonify({"error": f"Erro ao processar os dados: {e}"}), 400

    normallize_data(dados_usuario)
    
    try:
        imagem_gerada = generator_signature(dados_usuario)
        return send_file(
            imagem_gerada,
            mimetype='image/png',
            as_attachment=True,
            download_name=f"assinatura_{dados_usuario['nome']}.png"
        )

    except Exception as e:
        # Use o logger da aplicação para registrar o erro no servidor
        current_app.logger.error(f"Ocorreu um erro ao gerar a imagem: {e}")
        return jsonify({"error": "Ocorreu um erro interno no servidor. Por favor, contate o suporte."}), 500