from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lualinde'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/dicas')
def dicas():
    tips = [
        "Desligue luzes ao sair de um cômodo.",
        "Use lâmpadas de LED.",
        "Desligue aparelhos eletrônicos da tomada quando não estiverem em uso.",
        "Aproveite a luz natural.",
        "Mantenha portas e janelas fechadas quando o ar-condicionado estiver ligado.",
    ]
    
    return render_template('dicas.html', tips=tips)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == "usuario@example.com" and senha == "senha123":
            flash('Login realizado com sucesso!', 'sucess')
            return redirect(url_for('index'))
        
        flash('Nome de úsuario ou senha incorretos', 'danger')
            
    return render_template('login.html')



@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        flash('Cadastro realizado com sucesso!', 'sucess')
        return redirect(url_for('login'))
    return render_template('cadastro.html')


    

@app.route('/componentes')
def componentes():

    adms = [{'nome': 'Ingrid Leticia','imagem': 'ingrid.jpg'},
              {'nome': 'Jonas Nogueira','imagem': 'jonas.jpg'},
              {'nome': 'Luanny Martins','imagem': 'lua.jpg'},
              {'nome': 'Ryan Kauê','imagem': 'ryan.jpg'},
            ]
    return render_template('componentes.html', adms=adms)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/metas')
def metas():
    return render_template('metas.html') 

@app.route('/ideal_de_consumo')
def ideal_de_consumo():
    return render_template('ideal_de_consumo.html')


