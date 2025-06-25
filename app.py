from flask import Flask, request, jsonify, send_file, render_template
from validacao_dados import validar_dados
from normalizacao import normallizar_dados
from gerador_assinatura import gerar_assinatura

app = Flask(__name__)

@app.route('/') 
def form():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def receber_dados():
    try:        
        dados_usuario = request.get_json()
        if dados_usuario is None:
            return jsonify({"error": "Nenhum dado recebido"}), 400

        is_valid, mensagem_erro = validar_dados(dados_usuario)
        if not is_valid:
            return jsonify({"erro": mensagem_erro}), 400

    except Exception as e:
        return jsonify({"error": f"Erro ao processar os dados: {e}"}), 400

    normallizar_dados(dados_usuario)
    
    try:
        imagem_gerada = gerar_assinatura(dados_usuario)
        return send_file(
            imagem_gerada,
            mimetype='image/png',
            as_attachment=True,
            download_name=f"assinatura_{dados_usuario['nome']}.png"
        )

    except Exception as e:
        app.logger.error(f"Ocorreu um erro inesperado: {e}")
        return jsonify({"error": "Ocorreu um erro interno no servidor. Por favor, contate o suporte."}), 500

# if __name__ == '__main__':
#     app.run(debug=False)
#     app.run(host='0.0.0.0', port=5000, debug=False)