from xml.etree.ElementInclude import include

from flask import Flask, render_template, request, url_for, flash, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lualinde'


@app.route('/')
def index():
    return render_template('dashboard.html', include_sidebar=True, include_header=True)

@app.route('/dicas')
def dicas():
    tips = [
        "Desligue luzes ao sair de um cômodo.",
        "Use lâmpadas de LED.",
        "Desligue aparelhos eletrônicos da tomada quando não estiverem em uso.",
        "Aproveite a luz natural.",
        "Mantenha portas e janelas fechadas quando o ar-condicionado estiver ligado.",
    ]

    return render_template('dicas.html', tips=tips, include_sidebar=True, include_header=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == "usuario@example.com" and senha == "senha123":
            session['logged_in'] = True
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))

        flash('Nome de usuário ou senha incorretos', 'error')

    return render_template('login.html', include_sidebar=False, include_header=False)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html', include_sidebar=False, include_header=False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', include_sidebar=False, include_header=False), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', include_sidebar=False, include_header=False), 500


@app.route('/metas')
def metas():
    return render_template('metas.html', include_sidebar=True, include_header=True)


@app.route('/ideal_de_consumo')
def ideal_de_consumo():
    return render_template('ideal_de_consumo.html', include_sidebar=True, include_header=True)


@app.route('/logout')
def logout():
    session.clear()
    flash('Você foi deslogado', 'success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
