from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')
app.env = os.getenv('env')
app.debug = os.getenv('debug')


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()

