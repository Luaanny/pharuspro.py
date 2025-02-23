from flask import Blueprint, request, redirect, url_for, render_template
from app.extensions.database import db
from app.models.Consumo import Consumo
from flask_login import current_user, login_required

consumo_bp = Blueprint('consumo', __name__)

@consumo_bp.route('/simulador', methods=['POST', 'GET'])
@login_required
def simulador():
    consumos = Consumo.query.all()  
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

        db.session.add(novo_consumo)
        db.session.commit()

    return redirect(url_for('consumo.simulador'))
