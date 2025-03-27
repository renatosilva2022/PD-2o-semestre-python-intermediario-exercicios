from flask import Flask
from app.alquimias import init_db

# Criação da aplicação Flask
app = Flask(__name__)

# Configurações básicas da aplicação
app.config['SECRET_KEY'] = 'PD12345678'  # Chave secreta atualizada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/microblog.db'

# Inicializa o banco de dados com a aplicação
init_db(app)

# Importa as rotas para garantir que sejam registradas
import app.routes

if __name__ == '__main__':
    # Executa a aplicação em modo de desenvolvimento
    app.run(debug=True)