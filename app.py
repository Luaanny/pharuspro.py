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
    return render_template('dicas.html')



@app.route('/login')
def login():
    return render_template('login.html')

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
   