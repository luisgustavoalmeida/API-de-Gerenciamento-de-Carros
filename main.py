# Importar as bibliotecas necessárias
from flask import Flask, make_response, jsonify, request
from data import Carros  # Simula um banco de dados


# Criar uma instância do aplicativo Flask
app = Flask(__name__)

# Configuração para desativar a ordenação das chaves JSON
app.config['JSON_SORT_KEYS'] = False


# Definir uma rota para lidar com solicitações GET para /carros
@app.route('/carros', methods=['GET'])
def get_carros():
    try:
        # Criar uma resposta JSON que contém uma mensagem e os dados da lista de carros
        return make_response(
            jsonify(
                mensagem='Lista de carros.',
                dados=Carros
            )
        )
    except Exception as e:
        # Tratar outros erros desconhecidos retornando uma resposta 500 Internal Server Error
        return make_response(
            jsonify(
                mensagem='Erro interno do servidor: ' + str(e),
            ),
            500
        )
# Definir uma rota para lidar com solicitações GET para /carros/<int:id>
@app.route('/carros/<int:id>', methods=['GET'])
def get_carro_by_id(id):
    try:
        # Pesquisar o carro com a ID fornecida na lista de carros
        carro_encontrado = None
        for carro in Carros:
            if carro['id'] == id:
                carro_encontrado = carro
                break

        if carro_encontrado:
            # Se o carro for encontrado, retornar as informações do carro
            return make_response(
                jsonify(
                    mensagem='Carro encontrado.',
                    dados=carro_encontrado
                )
            )
        else:
            # Se o carro não for encontrado, retornar uma resposta 404 Not Found
            return make_response(
                jsonify(
                    mensagem='Carro não encontrado.'
                ),
                404
            )
    except Exception as e:
        # Tratar outros erros desconhecidos retornando uma resposta 500 Internal Server Error
        return make_response(
            jsonify(
                mensagem='Erro interno do servidor: ' + str(e),
            ),
            500
        )


# Definir uma rota para lidar com solicitações POST para /carros
@app.route('/carros', methods=['POST'])
def create_carro():
    try:
        # Obter o JSON da solicitação POST, que deve conter os dados do novo carro
        carro = request.json

        # Adicionar o carro à lista de carros (presumindo que a lista Carros seja definida em 'bd')
        Carros.append(carro)

        # Criar uma resposta JSON que confirma o cadastro do carro e inclui os dados do carro cadastrado
        return make_response(
            jsonify(
                mensagem='Carro cadastrado com sucesso.',
                dados=carro
            )
        )
    except ValueError as e:
        # Tratar erros de validação retornando uma resposta 400 Bad Request
        return make_response(
            jsonify(
                mensagem='Erro de validação: ' + str(e),
            ),
            400
        )
    except Exception as e:
        # Tratar outros erros desconhecidos retornando uma resposta 500 Internal Server Error
        return make_response(
            jsonify(
                mensagem='Erro interno do servidor: ' + str(e),
            ),
            500
        )

# Definir uma rota para lidar com solicitações DELETE para /carros/<int:id>
@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    try:
        # Procurar o carro com a ID fornecida na lista de carros
        carro_encontrado = None
        for carro in Carros:
            if carro['id'] == id:
                carro_encontrado = carro
                break

        if carro_encontrado:
            # Se o carro for encontrado, removê-lo da lista de carros
            Carros.remove(carro_encontrado)

            # Criar uma resposta JSON que confirma a exclusão do carro
            return make_response(
                jsonify(
                    mensagem='Carro excluído com sucesso.',
                    dados=carro_encontrado
                )
            )
        else:
            # Se o carro não for encontrado, retornar uma resposta 404 Not Found
            return make_response(
                jsonify(
                    mensagem='Carro não encontrado.'
                ),
                404
            )
    except Exception as e:
        # Tratar outros erros desconhecidos retornando uma resposta 500 Internal Server Error
        return make_response(
            jsonify(
                mensagem='Erro interno do servidor: ' + str(e),
            ),
            500
        )

# Iniciar o servidor Flask
app.run()
