from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import User
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST' and form.validate:
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


# Login function
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(email=form.email.data).first()

        if user:  # если юзер есть в базе данных
            if check_password_hash(user.password,
                                   form.password.data):
                session['logged_in'] = True
                session['email'] = user.email
                session['username'] = user.name
                return redirect(url_for('index_page'))
            else:  # если пользователя нет или пароль неправильный
                return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index_page'))
