from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '7562'


def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_data():
    conn = get_db()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    return posts


def get_post(post_id):
    conn = get_db()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    if post is None:
        abort(404)
    else:
        return post


@app.route('/')
def home():
    posts = get_data()
    return render_template('homepage.html', posts=posts)


@app.route('/posts/<int:post_id>')
def single_post(post_id):
    post = get_post(post_id)
    return render_template('post_template.html', post=post)


@app.route('/user/<name>')
def user_profile(name):
    return render_template('user_profile.html', user_name=name)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Error, title is required!')
        else:
            conn = get_db()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))

    return render_template('post_creation.html')


if __name__ == '__main__':
    app.run(debug=True)
