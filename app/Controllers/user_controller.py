from functools import wraps 
from flask import abort, Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.extensions.database import db
from app.models.User import User
from app.models.Consumo import Consumo
from flask_login import current_user, login_required, logout_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    consumos = Consumo.query.filter_by(user_id=current_user.id).all()

    consumo_mensal = sum(consumo.consumo_mensal for consumo in consumos)
    consumo_mensal = round(consumo_mensal, 2)

    return render_template("pages/profile.html", include_header=True, consumo_mensal=consumo_mensal)

@user_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    username = request.form.get('username')
    email = request.form.get('email')

    if not username or not email:
        return flash('Todos os campos são obrigatórios', 'error')

    if User.query.filter_by(email=email).first() and current_user.email != email:
        return flash('Esse email já está em uso', 'error')

    current_user.username = username
    current_user.email = email
    db.session.commit()

    flash("Usuário atualizado com sucesso", "success")
    return redirect(url_for('user.profile'))

@user_bp.route('/user/delete/<int:user_id>', methods=["DELETE"])
@login_required
def delete(user_id):
    if current_user.id != user_id:
        return jsonify({"error": "unauthorized"}), 403

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "user not found"}), 404

    logout_user()

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"user {user.username} deletado com sucesso!"}), 200, flash(
        f"user {user.username} deletado com sucesso!")

def role_required(role):
    def decorador(func):
        @wraps(func)
        def wraps_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return func(*args, **kwargs)
        return wraps_function
    return decorador
