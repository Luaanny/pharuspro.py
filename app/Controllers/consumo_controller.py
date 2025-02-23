from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.extensions.database import db
from app.models.Consumo import Consumo
from flask_login import current_user, login_required
import random

consumo_bp = Blueprint('consumo', __name__)
tips = [
        "Desligue luzes ao sair de um cômodo.",
        "Use lâmpadas de LED.",
        "Desligue aparelhos eletrônicos da tomada quando não estiverem em uso.",
        "Aproveite a luz natural.",
        "Mantenha portas e janelas fechadas quando o ar-condicionado estiver ligado.",
    ]

@consumo_bp.route('/simulador', methods=['GET'])
@login_required
def simulador():
    consumos = Consumo.query.filter_by(user_id=current_user.id).all()
    return render_template('pages/simulador.html', consumos=consumos, include_header=True, include_sidebar=True)

@consumo_bp.route('/device_register', methods=['POST'])
def device_register():
    if request.method == 'POST':
        aparelho = request.form['aparelho']
        potency = float(request.form['potency'])
        time_interval = float(request.form['time_interval'])
        consumo_mensal = (potency * time_interval * 30) / 1000

        novo_consumo = Consumo(
            aparelho=aparelho,
            potency=float(potency),
            time_interval=float(time_interval),
            consumo_mensal=float(consumo_mensal),
            user=current_user
        )

        existing_consumo = Consumo.query.filter_by(
            user_id=current_user.id,
            aparelho=novo_consumo.aparelho,
            potency=novo_consumo.potency,
            time_interval=novo_consumo.time_interval
        ).first()

        if not existing_consumo:
            db.session.add(novo_consumo)
            db.session.commit()
            flash('Aparelho registrado com sucesso', 'success')
            flash(f'{random.choice(tips)}', 'tip')
        else:
            flash('Aparelho já registrado', 'error')


    return redirect(url_for('consumo.simulador'))
