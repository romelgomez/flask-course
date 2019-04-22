from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '321SD5A1SD321ASD5A1'

todos = ['TODO 1', 'TODO 3' , 'TODO 3']

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

@app.route('/hello')
def hello():
    # user_ip = request.remote_addr
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    # return 'Hello your IP is: {}'.format(user_ip)  

    context = {
        'user_ip':user_ip,
        'todos': todos
    }

    return render_template('hello.html', **context)