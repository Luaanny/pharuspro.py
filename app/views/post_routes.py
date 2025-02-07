from datetime import datetime

from flask import Blueprint, render_template, redirect, redirect, url_for, request, flash
from flask_login import current_user, login_required

from app.extensions.database import db
from app.models.Consumo import Consumo
from app.Controllers.user_controller import role_required

post_bp = Blueprint('post', __name__)


@post_bp.route('/')
def index():
    return render_template("pages/dashboard.html", include_sidebar=True, include_header=True)


@post_bp.route('/metas', methods=['GET', 'POST'])
def metas():
    consumo_mensal = db.session.query(Consumo).filter_by(user_id=current_user.id).order_by(Consumo.date.desc()).first()
    print(
        f"Consumo mensal recuperado do banco: {consumo_mensal.consumo_mensal if consumo_mensal else 'Nenhum consumo encontrado'}")
    faixa_min = None
    faixa_max = None

    if consumo_mensal is not None:
        faixa_min = consumo_mensal.consumo_mensal - 20
        faixa_max = consumo_mensal.consumo_mensal + 20

    return render_template('pages/metas.html', include_sidebar=True, include_header=True, consumo_mensal=consumo_mensal,
                           faixa_min=faixa_min, faixa_max=faixa_max)


@post_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    can_edit = current_user.role == 'admin' 

    if request.method == 'POST' and can_edit:
        username = request.form.get('username')
        email = request.form.get('email')
        role = request.form.get('role')

        if not username or not email or not role:
            flash("Todos os campos são obrigatórios.", "error")
        else:
            current_user.username = username
            current_user.email = email
            current_user.role = role
            db.session.commit()
            flash("Perfil atualizado com sucesso!", "success")

        return redirect(url_for('post.profile'))

    return render_template("pages/profile.html", include_header=True, can_edit=can_edit)


@post_bp.route('/simulador', methods=['POST', 'GET'])
def simulador():
    consumo_mensal = None

    if request.method == 'POST':
        try:
            potency = float(request.form['potency'])
            time_interval = float(request.form['time_interval'])
            tariff = float(request.form['tariff'])

            consumo_mensal = ((potency * time_interval * 30) / 1000) * tariff

            novo_consumo = Consumo(
                date=datetime.now(),
                potency=potency,
                time_interval=time_interval,
                tariff=tariff,
                user=current_user,
                consumo_mensal=consumo_mensal,
            )

            db.session.add(novo_consumo)
            db.session.commit()

            print(f"Consumo mensal calculado e armazenado na sessão: {consumo_mensal}")

            return redirect(url_for('post.metas'))

        except ValueError:
            return render_template('pages/simulador.html',
                                   message="Por favor, insira valores válidos para todos os campos.")

    return render_template('pages/simulador.html')


@post_bp.route('/ideal_de_consumo')
def ideal_de_consumo():
    return render_template('pages/ideal_de_consumo.html', include_sidebar=True, include_header=True)


@post_bp.route('/dicas')
def dicas():
    tips = [
        "Desligue luzes ao sair de um cômodo.",
        "Use lâmpadas de LED.",
        "Desligue aparelhos eletrônicos da tomada quando não estiverem em uso.",
        "Aproveite a luz natural.",
        "Mantenha portas e janelas fechadas quando o ar-condicionado estiver ligado.",
    ]

    return render_template('pages/dicas.html', tips=tips, include_sidebar=True, include_header=True)


@post_bp.route('/admin')
@login_required
@role_required('admin')
def admin_dashboard():
    return "Bem-vindo ao painel de administração!"


@post_bp.route('/User')
@login_required
def user_dashboard():
    return f'Olá {current_user.username}! Este é o painel do usuário.'
