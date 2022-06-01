from flask import Blueprint, redirect, render_template, url_for

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')

