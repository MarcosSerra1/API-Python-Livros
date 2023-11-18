from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1,
     'titulo': 'Harry Potter e a Pedra Filosofal',
     'autor': 'J.K. Rowling'
     },

    {'id': 2,
     'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
     'autor': 'J.R.R. Tolkien'
     },

    {'id': 3,
     'titulo': 'Harry Potter e a Câmara Secreta',
     'autor': 'J.K. Rowling'
     },

    {'id': 4,
     'titulo': 'O Senhor dos Anéis: As Duas Torres',
     'autor': 'J.R.R. Tolkien'
     },

    {'id': 5,
     'titulo': 'Harry Potter e o Prisioneiro de Azkaban',
     'autor': 'J.K. Rowling'
     },

    {'id': 6,
     'titulo': 'O Senhor dos Anéis: O Retorno do Rei',
     'autor': 'J.R.R. Tolkien'
     },
    # Adicione mais livros conforme necessário
]  # Essa lista de dicionários é nossa base de dados.


# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar livros por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar livro
@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Excluir livros
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
