from functools import wraps
from flask import abort, Blueprint, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions.database import db
from app.models.User import User
from flask_login import current_user, login_required, logout_user, login_user
from app.extensions.flask_login import lm

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@lm.user_loader
def load_user(id):
    return User.query.get(id)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, senha):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('post.index'))

        flash('Email ou senha incorretos', 'error')

    return render_template('auth/login.html', include_sidebar=False, include_header=False)

@auth_bp.route('/cadastrar', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado', 'error')
            return redirect(url_for('auth_bp.register'))

        hashed_password = generate_password_hash(senha, method='pbkdf2:sha256')
        new_user = User(username=nome, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('post.index'))

    return render_template('auth/cadastro.html', include_sidebar=False, include_header=False)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('auth_bp.login'))