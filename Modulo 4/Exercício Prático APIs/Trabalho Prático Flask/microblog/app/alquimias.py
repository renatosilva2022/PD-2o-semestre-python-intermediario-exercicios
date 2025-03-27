from flask_sqlalchemy import SQLAlchemy

# Inicialização do SQLAlchemy
db = SQLAlchemy()

# Função para inicializar o banco de dados com a aplicação Flask
def init_db(app):
    db.init_app(app)

# Funções auxiliares para interagir com o banco de dados
def create_all():
    """Cria todas as tabelas no banco de dados."""
    db.create_all()

def drop_all():
    """Remove todas as tabelas do banco de dados."""
    db.drop_all()

def add_and_commit(instance):
    """
    Adiciona uma nova instância ao banco de dados e faz commit.
    :param instance: Instância de um modelo (ex.: User, Post).
    """
    db.session.add(instance)
    db.session.commit()

def delete_and_commit(instance):
    """
    Remove uma instância do banco de dados e faz commit.
    :param instance: Instância de um modelo (ex.: User, Post).
    """
    db.session.delete(instance)
    db.session.commit()

def create_post(body, author):
    """
    Cria um novo post no banco de dados.
    :param body: Conteúdo do post.
    :param author: Usuário autenticado.
    """
    new_post = Post(body=body, author=author)
    db.session.add(new_post)
    db.session.commit()
    return new_post


def get_timeline():
    """
    Retorna os 5 posts mais recentes.
    """
    return Post.query.order_by(Post.timestamp.desc()).limit(5).all()