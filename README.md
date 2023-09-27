# Flask
# API de Gerenciamento de Carros

Esta é uma API simples de gerenciamento de carros construída com o Flask. A API permite listar carros existentes e cadastrar novos carros.

## Instalação

Certifique-se de ter o Python 3.11 instalado em sua máquina. Você pode instalar as dependências do projeto com o seguinte comando:

```bash
pip install -r requirements.txt
Executando o Servidor
Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

bash
Copy code
python main.py
O servidor estará disponível em http://127.0.0.1:5000/ por padrão.

Rotas da API
Listar Carros (GET /carros)
Esta rota permite listar todos os carros existentes.

Exemplo de Requisição:

bash
Copy code
curl -X GET http://127.0.0.1:5000/carros
Exemplo de Resposta:

json
Copy code
{
    "mensagem": "Lista de carros.",
    "dados": [
        {
            "ano": 1999,
            "id": 1,
            "marca": "Fiat",
            "modelo": "Marea"
        },
        {
            "ano": 1999,
            "id": 2,
            "marca": "Fiat",
            "modelo": "Uno"
        }
    ]
}
Cadastrar Carro (POST /carros)
Esta rota permite cadastrar um novo carro.

Exemplo de Requisição:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"marca": "Ford", "modelo": "Focus", "ano": 2020}' http://127.0.0.1:5000/carros
Exemplo de Resposta:

json
Copy code
{
    "mensagem": "Carro cadastrado com sucesso.",
    "dados": {
        "ano": 2020,
        "id": 3,
        "marca": "Ford",
        "modelo": "Focus"
    }
}
Tratamento de Requisições Inválidas
A API lida com requisições inválidas retornando códigos de status HTTP apropriados e mensagens de erro descritivas. Por exemplo, uma tentativa de cadastrar um carro sem especificar a marca ou o modelo resultará em um código de status 400 Bad Request e uma mensagem de erro.
