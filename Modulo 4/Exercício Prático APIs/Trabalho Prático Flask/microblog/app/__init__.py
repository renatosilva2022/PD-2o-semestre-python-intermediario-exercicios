from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicialização do aplicativo
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PD12345678'  # Chave secreta atualizada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/microblog.db'

# Configuração do banco de dados
db = SQLAlchemy(app)

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Carregar usuário
@login_manager.user_loader
def load_user(user_id):
    from app.models.models import User
    return User.query.get(int(user_id))

# Importar rotas ao final para evitar importações circulares
from app import routes