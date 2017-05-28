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
    amount = StringField('amount', validators=[DataRequired()])
    interest = SelectField(u'Interest', coerce=int)
    total_payable = StringField('total_payable', default=0)
    payment = StringField('payment', default=0)
    total_payment = StringField('total_payment', default=0)
    outstanding_balance = StringField('outstanding_balance', default=0)

class EditForm(Form):
    customer_name = SelectField(u'Customers', coerce=int)
    comaker_name = SelectField(u'Customers', coerce=int)
    date_release = StringField(
        'date_release')
    date_due = StringField(
        'date_due')
    fully_paid_on = StringField(
        'fully_paid_on')
    amount = StringField('amount')
    interest = SelectField(u'Interest', coerce=int)
    total_payable = StringField('total_payable')
    payment = StringField('payment')
    total_payment = StringField('total_payment')
    outstanding_balance = StringField('outstanding_balance')