from wtforms import Form, BooleanField, \
    StringField, PasswordField, validators, \
    TextAreaField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    validators.Length(
                                    min=7, max=50)
                                    ])
    password = PasswordField('Password',
                             validators=[DataRequired()])


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(),
                                             validators.Length(
                                                 min=9, max=12)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Password', validators=[DataRequired(),
                                                    validators.EqualTo('password')])