from flask_wtf import Form
from wtforms import StringField, IntegerField, FormField
from wtforms.validators import DataRequired, Length, Email

class TelephoneForm(Form):
    country_code = IntegerField('Country Code', validators=[DataRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators=[DataRequired()])
    number       = StringField('Number', validators=[DataRequired()])

class AddForm(Form):
    first_name = StringField(
        'firstname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'lastname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    mobile_phone = FormField(TelephoneForm)

class EditForm(Form):
    first_name = StringField(
        'firstname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'lastname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    mobile_phone = FormField(TelephoneForm)