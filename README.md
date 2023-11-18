# API de Gerenciamento de Livros

Esta é uma API simples construída usando Flask e SQLAlchemy para gerenciar informações sobre livros. A API permite a criação, leitura, atualização e exclusão de livros em um banco de dados SQLite.

## Pré-requisitos

- [Python](https://www.python.org/) instalado
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/) instalado
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) instalado

você pode instalar as bibliotecas usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

O banco de dados utilizado é o SQLite. Para criar o banco de dados e suas tabelas, execute o seguinte comando no terminal:

```bash
python app.py
```

## Endpoints

### 1. Obter todos os livros

- **URL:** `/livros`
- **Método:** `GET`
- **Descrição:** Retorna uma lista de todos os livros cadastrados.

### 2. Obter livro por ID

- **URL:** `/livros/<int:id>`
- **Método:** `GET`
- **Parâmetro:** `id` (inteiro)
- **Descrição:** Retorna informações sobre um livro específico com base no ID fornecido.

### 3. Editar livro por ID

- **URL:** `/livros/<int:id>`
- **Método:** `PUT`
- **Parâmetro:** `id` (inteiro)
- **Descrição:** Edita as informações de um livro com base no ID fornecido. O corpo da requisição deve conter os dados a serem atualizados.

### 4. Criar livro(s)

- **URL:** `/livros`
- **Método:** `POST`
- **Descrição:** Cria um novo livro ou vários livros. O corpo da requisição pode ser um dicionário com informações de um livro ou uma lista de dicionários para criar vários livros de uma vez.

### 5. Excluir livro por ID

- **URL:** `/livros/<int:id>`
- **Método:** `DELETE`
- **Parâmetro:** `id` (inteiro)
- **Descrição:** Exclui um livro com base no ID fornecido.

## Como Executar

Execute o arquivo `app.py` para iniciar o servidor local. Certifique-se de que o Flask e o SQLAlchemy estão instalados no ambiente virtual.

```bash
python app.py
```

A API estará disponível em [http://localhost:5000](http://localhost:5000).

Lembre-se de que esta é uma aplicação de exemplo e deve ser adaptada conforme necessário para atender aos requisitos específicos do seu projeto.
