from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )

class EditPasswordForm(Form):

    password = PasswordField(
        'old password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    newpassword = PasswordField(
        'newpassword',
        validators=[
            DataRequired(), Length(min=6, max=25)
        ]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(), EqualTo('newpassword', message='Passwords must match.')
        ]
    )

class EditEmailForm(Form):
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )

    newemail = StringField(
        'new email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )

    confirm = StringField(
        'confirm email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40), EqualTo('newemail', message='Emails must match.')]
    )