from coinage import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(150), unique=False)
    address = db.Column(db.String(80))
    mobile_phone = db.Column(db.String(80))

    def __init__(self, first_name=None, last_name=None, email=None, address=None, mobile_phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.mobile_phone = mobile_phone

