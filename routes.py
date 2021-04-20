from app import app, db
from flask import render_template, request, redirect, url_for
from models import User
from forms import LoginForm, RegisterForm
from werkzeug import generate_password_hash, check_password_hash


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # создаю пароль (шифрованный)
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')

        # создаю пользователя
        new_user = User(
            name=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            password=hashed_password)

        # сохраняю пользователя в базе
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index_page'))
    else:
        return render_template('register.html', form=form)
