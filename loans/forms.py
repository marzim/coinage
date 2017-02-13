from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import Length, Email, InputRequired, DataRequired

class AddForm(Form):
    customer_name = SelectField(u'Customers', coerce=int)

    date_release = StringField(
        'date_release')
    date_due = StringField(
        'date_release')
    fully_paid_on = StringField(
        'fully_paid_on')
    amount = FloatField('amount')
    interest = SelectField(u'Interest', coerce=int)
    total_payable = FloatField('total_payable')
    payment = FloatField('payment')
    total_payment = FloatField('total_payment')
    outstanding_balance = FloatField('outstanding_balance')

class EditForm(Form):
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