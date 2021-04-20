from app import app, db
from flask import render_template
from models import User
from forms import LoginForm, RegisterForm


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    return render_template('register.html')
