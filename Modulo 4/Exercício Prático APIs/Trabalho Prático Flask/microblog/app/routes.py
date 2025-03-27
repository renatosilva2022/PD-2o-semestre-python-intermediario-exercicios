from flask import render_template, redirect, url_for, request, flash
from app.models.models import User, Post, db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    if current_user.is_authenticated:
        posts = Post.query.order_by(Post.timestamp.desc()).limit(5).all()
        return render_template('index.html', posts=posts)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Email ou senha inválidos.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        foto = request.form['foto']
        bio = request.form['bio']

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email já cadastrado!')
            return redirect(url_for('cadastro'))

        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            foto=foto,
            bio=bio
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        new_post = Post(body=body, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        new_post = alquimias.create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')