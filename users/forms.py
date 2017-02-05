from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class AddForm(Form):
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

    can_create = BooleanField('Create', default=False)
    can_update = BooleanField('Update', default=False)
    can_delete = BooleanField('Delete', default=False)

class EditForm(Form):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    can_create = BooleanField('Create', default=False)
    can_update = BooleanField('Update', default=False)
    can_delete = BooleanField('Delete', default=False)
