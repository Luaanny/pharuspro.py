from flask import Blueprint, render_template

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
def index():
    return render_template("pages/dashboard.html", include_sidebar = True, include_header = True)

@post_bp.route('/metas')
def metas():
    return render_template('pages/metas.html', include_sidebar=True, include_header=True)

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
