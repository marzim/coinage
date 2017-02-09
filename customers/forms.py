from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class AddForm(Form):
    first_name = StringField(
        'firstname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'lastname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    number_shares = IntegerField('numbershares',
                                 validators=[DataRequired()])
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    mobile_phone = StringField(
        'mobilephone',
        validators=[DataRequired(), Length(min=3, max=25)]
    )

class EditForm(Form):
    first_name = StringField(
        'firstname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'lastname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    number_shares = IntegerField('numbershares',
                                 validators=[DataRequired()])
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    mobile_phone = StringField(
        'mobilephone',
        validators=[DataRequired(), Length(min=3, max=25)]
    )