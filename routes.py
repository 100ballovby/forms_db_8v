from app import app
from flask import render_template


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/register')
def register_page():
    return render_template('register.html')
