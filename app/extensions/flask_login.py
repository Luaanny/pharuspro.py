from flask_login import LoginManager
from flask import render_template

lm = LoginManager()

@lm.unauthorized_handler
def unauthorized():
    
    return render_template('errors/401.html'), 401
