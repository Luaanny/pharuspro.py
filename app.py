from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lualinde'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

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



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/Pagina_inicial', methods=['POST'])
def Pagina_inicial():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == 'admin' and senha == 'senha123':
        return render_template ('index.html')
    else: 
        flash('Dados incorretos. Login ou senha inválidos', 'danger')
        flash('tente novamente', 'warning')
        return redirect(url_for('login'))

@app.route('/componentes')
def componentes():

    adms = [{'nome': 'Ingrid Leticia','imagem': 'ingrid.jpg'},
              {'nome': 'Jonas Nogueira','imagem': 'jonas.jpg'},
              {'nome': 'Luanny Martins','imagem': 'lua.jpg'},
              {'nome': 'Ryan Kauê','imagem': 'ryan.jpg'},
            ]
    return render_template('componentes.html', adms=adms)
   