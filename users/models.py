from coinage import db
from coinage import bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(150), unique=False)
    password = db.Column(db.String(150))
    can_create = db.Column(db.Boolean, default=False)
    can_update = db.Column(db.Boolean, default=False)
    can_delete = db.Column(db.Boolean, default=False)

    def __init__(self, can_create=False, can_update=False, can_delete=False, name=None, email=None, password=None):
        self.set_property(can_create, can_update, can_delete, name, email, password)

    def set_property(self, can_create=False, can_update=False, can_delete=False, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.can_create = can_create
        self.can_update = can_update
        self.can_delete = can_delete

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
