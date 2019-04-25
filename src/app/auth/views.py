from flask import render_template, session, flash, redirect, url_for
from src.app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data
        flash('Nombre de usuario regitrado con éxito')


    return render_template('login.html', **context)


    