from flask import Blueprint, request, jsonify, send_file, current_app

from data_validation import validateData
from normalize import normalizeData
from signature_generator import signatureGenerator

api_route = Blueprint('api_route', __name__)

@api_route.route('/api', methods=['POST'])
def receiveData():
    try:
        userData = request.get_json()
        if userData is None:
            return jsonify({"error": "Nenhum dado recebido"}), 400

        isValid, mensageErro = validateData(userData)
        if not isValid:
            return jsonify({"erro": mensageErro}), 400

    except Exception as e:
        return jsonify({"error": f"Erro ao processar os dados: {e}"}), 400

    normalizedUserData = normalizeData(userData)
    
    try:
        generatedImage = signatureGenerator(normalizedUserData)
        return send_file(
            generatedImage,
            mimetype='image/png',
            as_attachment=True,
            download_name="assinatura.png"
        )

    except Exception as e:
        # Use o logger da aplicação para registrar o erro no servidor
        current_app.logger.error(f"Ocorreu um erro ao gerar a imagem: {e}")
        return jsonify({"error": "Ocorreu um erro interno no servidor. Por favor, contate o suporte."}), 500