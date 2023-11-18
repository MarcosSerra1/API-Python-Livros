from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
db = SQLAlchemy(app)


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)


# Criação do banco de dados
with app.app_context():
    db.create_all()


# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = Livro.query.all()
    return jsonify([{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor} for livro in livros])


# Consultar livros por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    livro = Livro.query.get(id)
    if not livro:
        return {'message': 'Livro não encontrado'}, 404
    return jsonify({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor})


# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro = Livro.query.get(id)
    if not livro:
        return {'message': 'Livro não encontrado'}, 404

    livro_alterado = request.get_json()
    livro.titulo = livro_alterado.get('titulo', livro.titulo)
    livro.autor = livro_alterado.get('autor', livro.autor)

    db.session.commit()
    return jsonify({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor})


# Criar livro (suporta criação de um ou vários livros)
@app.route('/livros', methods=['POST'])
def criar_livros():
    dados = request.get_json()

    # Verifica se os dados são uma lista
    if isinstance(dados, list):
        novos_livros = []
        for dados_livro in dados:
            novo_livro = Livro(titulo=dados_livro.get('titulo'), autor=dados_livro.get('autor'))
            db.session.add(novo_livro)
            novos_livros.append({'id': novo_livro.id, 'titulo': novo_livro.titulo, 'autor': novo_livro.autor})

        db.session.commit()
        return jsonify(novos_livros)

    # Se os dados não forem uma lista, cria apenas um livro
    elif isinstance(dados, dict):
        novo_livro = Livro(titulo=dados.get('titulo'), autor=dados.get('autor'))
        db.session.add(novo_livro)
        db.session.commit()
        return jsonify({'id': novo_livro.id, 'titulo': novo_livro.titulo, 'autor': novo_livro.autor})

    # Se os dados não forem uma lista nem um dicionário, retorna um erro
    return jsonify({'message': 'Os dados devem ser uma lista de livros ou um livro'}), 400


# Excluir livros
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    livro = Livro.query.get(id)
    if not livro:
        return {'message': 'Livro não encontrado'}, 404
    db.session.delete(livro)
    db.session.commit()
    return jsonify({'message': 'Livro excluído com sucesso'})


# Executa a aplicação na porta 5000 e com debug ativado
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
