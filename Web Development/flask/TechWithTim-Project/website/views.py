from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html')
