from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from flask import Flask, render_template, url_for, request, redirect
from flask_bcrypt import Bcrypt

from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')
app.env = os.getenv('env')
app.debug = os.getenv('debug')
app.database = os.getenv('database')
bcrypt = Bcrypt(app)


def load_db():
    conn = sqlite3.connect(app.database)
    conn.row_factory = sqlite3.Row
    return conn


class User(UserMixin):
    conn = load_db()
    id = ...
    name = ...
    email = ...
    password = ...


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return ...


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=('GET', 'POST'))
def login():
    conn = load_db()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = conn.execute('SELECT * FROM users')
        for row in data:
            if email == row['email'] and password == row['password']:
                return redirect(url_for('user_area'))

    return render_template('login.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    conn = load_db()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn.execute("INSERT INTO users (name, email, password) VALUES (?,?,?)", (name, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/user_area')
def user_area():
    return 'You was authenticated'


if __name__ == '__main__':
    app.run()
