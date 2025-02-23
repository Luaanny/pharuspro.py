from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify
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

        if 0 < time_interval <= 24 and potency > 0:
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
                flash(f'Aparelho {novo_consumo.aparelho} registrado com sucesso', 'success')
                flash(f'{random.choice(tips)}', 'tip')
            else:
                flash('Aparelho já registrado', 'error')

        else:
            flash('Tempo de uso ou potência inválidos', 'error')


    return redirect(url_for('consumo.simulador'))

@consumo_bp.route('/update_device/<int:consumo_id>', methods=['PUT'])
def update_device(consumo_id):
    data = request.get_json()

    potency = data.get('potency')
    time_interval = data.get('time_interval')
    consumo_mensal = (float(potency) * float(time_interval) * 30) / 1000

    consumo = Consumo.query.filter_by(user_id=current_user.id, id=consumo_id).first()
    if consumo:
        consumo.potency = float(potency)
        consumo.time_interval = float(time_interval)
        consumo.consumo_mensal = float(consumo_mensal)
        db.session.commit()
        return jsonify({"message": "Consumo atualizado com sucesso"}), 200, flash('Consumo atualizado com sucesso', 'success')
    else:
        return jsonify({"error": "Consumo não encontrado"}), 404, flash('Consumo não encontrado', 'error')


@consumo_bp.route('/consumo/delete/<int:consumo_id>', methods=['DELETE'])
@login_required
def delete(consumo_id):
    if request.method == 'DELETE':
        consumo = Consumo.query.get(consumo_id)

        db.session.delete(consumo)
        db.session.commit()

        return jsonify({"message": f"Aparelho {consumo.aparelho} deletado com sucesso!"}), 200, flash(
            f"aparelho {consumo.aparelho} deletado com sucesso!", 'success')