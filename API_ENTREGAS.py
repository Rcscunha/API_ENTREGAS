from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notificacao/entrega', methods=['POST'])
def receber_notificacao_entrega():
    # Verifica se a requisição possui os dados necessários
    if not request.json or 'id_entrega' not in request.json or 'status' not in request.json:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    # Obtém os dados da notificação
    id_entrega = request.json['id_entrega']
    status = request.json['status']

    # Aqui você pode processar a notificação como desejado, por exemplo, atualizando o status da entrega no banco de dados

    return jsonify({'message': 'Notificação recebida com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)