from coinage import db

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, unique=False)
    interest = db.Column(db.Float, unique=False)
    payment = db.Column(db.Float, unique=False)
    total_payable = db.Column(db.Float, unique=False)
    total_payment = db.Column(db.Float, unique=False)
    outstanding_balance = db.Column(db.Float, unique=False)
    fully_paid_on = db.Column(db.String(80))
    date_release = db.Column(db.String(80))
    date_due = db.Column(db.String(80))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))

    # def __init__(self, customer_id=0, amount=0, interest=0, payment=0, total_payable=0, total_payment=0, outstanding_balance=0, fully_paid_on=None, date_release=None, date_due=None):
    #     self.customer_id = customer_id
    #     self.amount = amount
    #     self.interest = interest
    #     self.payment = payment
    #     self.total_payable = total_payable
    #     self.total_payment = total_payment
    #     self.outstanding_balance = outstanding_balance
    #     self.fully_paid_on = fully_paid_on
    #     self.date_release = date_release
    #     self.date_due = date_due

class Interest(db.Model):
    __tablename__ = "interest"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    name = db.Column(db.String(50), unique=False)

    def __init__(self, name=None):
        self.name=name