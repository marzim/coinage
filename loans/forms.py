from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import Length, Email, InputRequired, DataRequired

class AddForm(Form):
    customer_name = SelectField(u'Customers', coerce=int)
    comaker_name = SelectField(u'Customers', coerce=int)
    date_release = StringField(
        'date_release')
    date_due = StringField(
        'date_release')
    amount = FloatField('amount')
    interest = SelectField(u'Interest', coerce=int)
    total_payable = FloatField('total_payable')
    payment = FloatField('payment')
    total_payment = FloatField('total_payment')
    outstanding_balance = FloatField('outstanding_balance')

class EditForm(Form):
    customer_name = SelectField(u'Customers', coerce=int)
    comaker_name = SelectField(u'Customers', coerce=int)
    date_release = StringField(
        'date_release')
    date_due = StringField(
        'date_due')
    fully_paid_on = StringField(
        'fully_paid_on')
    amount = FloatField('amount')
    interest = SelectField(u'Interest', coerce=int)
    total_payable = FloatField('total_payable')
    payment = FloatField('payment')
    total_payment = FloatField('total_payment')
    outstanding_balance = FloatField('outstanding_balance')