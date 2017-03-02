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


class Interest(db.Model):
    __tablename__ = "interest"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    name = db.Column(db.String(50), unique=False)

    def __init__(self, name=None):
        self.name=name