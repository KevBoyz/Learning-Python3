from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_data():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Result in a dict instead a tuple
    posts = conn.execute('SELECT * FROM posts').fetchall()
    return posts


@app.route('/')
def home():
    posts = get_data()
    return render_template('homepage.html', posts=posts)


@app.route('/bitches')
def bitches():
    return render_template('bitches.html')


@app.route('/user/<name>')
def user_profile(name):
    return render_template('user_profile.html', user_name=name)


if __name__ == '__main__':
    app.run(debug=True)
