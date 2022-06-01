from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()


def create_database(app):
    if not os.path.exists('website/database.db'):
        db.create_all(app=app)


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv('secret_key')
    app.env = os.getenv('env')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  # /auth/ -> /auth/lol

    from website.models import User, Note  # Just loading the classes

    create_database(app)

    return app



