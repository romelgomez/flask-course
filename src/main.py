from flask import Flask, request, make_response, redirect, render_template, session, flash, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest



app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '321SD5A1SD321ASD5A1'

todos = ['TODO 1', 'TODO 3' , 'TODO 3']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('hello')) 
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.remote_addr
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    # return 'Hello your IP is: {}'.format(user_ip)  
    username = session.get('username')

    login_form = LoginForm()

    context = {
        'user_ip':user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username,
    }



    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario regitrado con éxito')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)