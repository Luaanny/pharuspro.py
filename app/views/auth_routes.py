from flask import session, Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User
from app.extensions.database import db

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, senha):
            session['logged_in'] = True
            session['user_id'] = user.id
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('post.index'))

        flash('Nome de usuário ou senha incorretos', 'error')

    return render_template('auth/login.html', include_sidebar=False, include_header=False)

@auth_bp.route('/cadastrar', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado', 'error')
            return redirect(url_for('auth_bp.cadastrar'))

        hashed_password = generate_password_hash(request.form['senha'], method='pbkdf2:sha256')
        new_user = User(username=nome, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth_bp.login'))

    return render_template('auth/cadastro.html', include_sidebar=False, include_header=False)

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('auth_bp.login'))