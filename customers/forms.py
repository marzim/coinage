from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Length, Email, InputRequired, DataRequired

class AddForm(Form):
    first_name = StringField(
        'firstname',
        validators=[InputRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'lastname',
        validators=[InputRequired(), Length(min=3, max=25)]
    )
    number_shares = IntegerField('number_shares')
    email = StringField(
        'email',
        validators=[InputRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[InputRequired(), Length(min=3, max=25)]
    )
    mobile_phone = StringField(
        'mobile_phone',
        validators=[InputRequired(), Length(min=3, max=25)]
    )
    is_member = BooleanField('Member', default=False)

class EditCustomerForm(Form):
    first_name = StringField(
        'first_name',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        'last_name',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    number_shares = IntegerField('number_shares')
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    address = StringField(
        'address',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    mobile_phone = StringField(
        'mobile_phone',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    is_member = BooleanField('Member', default=False)