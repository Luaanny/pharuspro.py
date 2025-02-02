from flask import Blueprint, render_template, redirect, redirect, url_for, request
from app.models import User

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
def index():
    return render_template("pages/dashboard.html", include_sidebar = True, include_header = True)

@post_bp.route('/metas', methods=['GET', 'POST'])
def metas():
    return render_template('pages/metas.html', include_sidebar=True, include_header=True)

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
                user=current_user.id,
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
