from flask import Blueprint, render_template, request, flash, message_flashed
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html', text='skaokdjooj', user='Kevin')


@auth.route('/logout')
def logout():
    return 'lol'


@auth.route('/sing-up', methods=('GET', 'POST'))
def sing_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email to short need, be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('Name to short need, be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Passwords is to short, must be greater than 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
    return render_template('sing_up.html')
